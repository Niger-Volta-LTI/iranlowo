import csv
import gzip
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

