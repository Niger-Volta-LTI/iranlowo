import csv
import gzip
import unicodedata
from pathlib import Path


def is_valid_owé_format(text, n=4, is_file=False, **kwargs):  # Is this really needed? Maybe. Maybe not.
    """

    Args:
        text: The text to validate. Could be a text or file path. If file path, is_file should be True
        n: Separator count.
        is_file: True if text is path.

    Returns: True if the file format is valid.

    """
    if is_file:
        text = open(text).readlines() if not kwargs.get('is_zipped') else gzip.open(text).readlines()
    text = [line for line in text if line != '\n']
    return len(text) % n == 0


def convert_to_owé_format(path, sep=4, outpath=None, to_csv=False, **kwargs):
    """

    Args:
        to_csv:
        path:
        sep:
        outpath: Output path. Should be a list (of size 2) of directories to save the texts to i.e [yo_path, en_path]. If to_csv is True, should be a single csv path.
        kwargs:
             is_zipped : Boolean : Should be True if the file is zipped.
             csv_header: True if csv header should be written. Only needed if to_csv is True.


    Returns:

    """
    if kwargs.get('is_zipped', False):
        text = gzip.open(path).readlines()
    else:
        text = open(path).readlines()

    # @Todo: Raise an error (or should it be a warning?) if the text is not in the format available at https://github.com/Niger-Volta-LTI/youba-text/blob/master/Owe/youba_proverbs_out.txt.

    assert is_valid_owé_format(text, sep), "The file doesn't seem to have the valid Owé format. You can refer to the documentation on Owé for the correct format."

    def get_chunk(txt, n):
        """
        Divides the text in a file into a fixed number of chunks.

        Args:
            txt: The text to divide
            n: Chunk size

        Returns: Generator of fixed chunks.

        """
        for line in range(0, len(txt), n):
            yield txt[line:line + sep]

    text_chunks = list(get_chunk(text, sep))
    for index, _ in enumerate(text_chunks):
        try:
            yo = text_chunks[index][1]
            en = text_chunks[index][2]
            trans = text_chunks[index][3]
            if not outpath:
                yield yo, en, trans
            if to_csv:
                data = {'yo': yo, 'en': en, 'trans': trans}
                with open(outpath, 'w+') as f:
                    w = csv.DictWriter(f, data.keys())
                    if kwargs.get('csv_header', False):
                        w.writeheader()
                    w.writerow(data)
                    return True
            else:
                yo_dir = "{0}/yo_00{1}.txt".format(outpath[0], index)
                if Path(yo_dir).exists():
                    yo_dir = "{0}/yo_00{1}{1}.txt".format(outpath[0], index)
                    en_dir = "{0}/en_00{1}{1}.txt".format(outpath[1], index)
                else:
                    en_dir = "{0}/en_00{1}.txt".format(outpath[1], index)
                with open(yo_dir, 'w+') as writer:
                    writer.write(yo)
                with open(en_dir, 'w+') as writer:
                    en_text = "{0}{1}".format(en, trans)
                    writer.write(en_text)
        except IndexError:
            pass  # End of file reached


def strip_accents_text(text_string):
    """
    Converts the string to NFD, separates & returns only the base characters
    :param text_string:
    :return: input string without diacritic adornments on base characters
    """
    return "".join(
        c
        for c in unicodedata.normalize("NFD", text_string)
        if unicodedata.category(c) != "Mn"
    )


def strip_accents_file(filename, outfilename):
    """
    Reads filename containing diacritics, converts to NFC for consistency,
    then writes outfilename with diacritics removed
    :param filename:
    :param outfilename:
    :return: None
    """
    text = "".join(
        c for c in unicodedata.normalize("NFC", open(filename, encoding="utf-8").read())
    )
    try:
        f = open(outfilename, "w")
    except EnvironmentError:
        return False
    else:
        with f:
            f.write(strip_accents_text(text))
        return True


def normalize_diacritics_text(text_string):
    """Convenience wrapper to abstract away unicode & NFC"""
    return unicodedata.normalize("NFC", text_string)


def normalize_diacritics_file(filename, outfilename):
    """File based Convenience wrapper to abstract away unicode & NFC"""
    try:
        text = "".join(
            c
            for c in unicodedata.normalize(
                "NFC", open(filename, encoding="utf-8").read()
            )
        )
        with open(outfilename, "w", encoding="utf-8") as f:
            f.write(text)
    except EnvironmentError:
        return False
    else:
        return True


def split_corpus_on_symbol(filename, outfilename, symbol=","):
    """
    For yoruba blog (and probably bibeli mimo)

    Args: filenames for I/O and symbol to split lines on
    Returns: writes outputfile
    :param filename: input file
    :param outfilename: processed output file to write
    :param symbol: to split lines on
    :return: None, with side-effect of writing an outputfile
    """

    lines = tuple(open(filename, "r", encoding="utf-8"))

    min_words_to_split = 10
    min_words_in_utt = 5

    with open(outfilename, "w") as f:
        # split out heavily comma'd text :((
        for line in lines:
            if symbol in line:
                num_words = len(line.split())
                num_commas = line.count(symbol)
                curr_comma_position = line.index(symbol)
                num_words_ahead_of_curr_comma = len(line[0:curr_comma_position].split())

                curr_line = line
                while num_commas > 0:
                    if num_words < min_words_to_split:
                        # print(curr_line.strip())
                        f.write(curr_line)
                        break
                    if num_words >= min_words_to_split:
                        if (
                                num_words_ahead_of_curr_comma >= min_words_in_utt
                                and len(curr_line[curr_comma_position:].split())
                                >= min_words_in_utt
                        ):
                            f.write(curr_line[0:curr_comma_position] + "\n")

                            # update vars
                            curr_line = curr_line[curr_comma_position + 1:]
                            num_words = len(curr_line.split())
                            num_commas = num_commas - 1
                            if num_commas > 0:
                                curr_comma_position = curr_line.index(symbol)
                                num_words_ahead_of_curr_comma = len(
                                    curr_line[0:curr_comma_position].split()
                                )
                            else:
                                f.write(curr_line)
                        else:
                            # ignore too short comma (+= vs = on current comma position)
                            num_commas = num_commas - 1
                            if num_commas > 0:  # for say 3 commas
                                curr_comma_position += (
                                        curr_line[curr_comma_position + 1:].index(symbol)
                                        + 1
                                )
                                num_words_ahead_of_curr_comma = len(
                                    curr_line[0:curr_comma_position].split()
                                )
                            else:
                                f.write(curr_line)
                    else:
                        f.write(curr_line)
            else:
                f.write(line)


