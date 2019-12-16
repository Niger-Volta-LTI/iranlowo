import os
import re
import unicodedata
from collections import defaultdict

from pathlib import Path

from iranlowo.preprocessing import strip_accents_text

module_path = os.path.dirname(__file__)


def datapath(fname):
    return os.path.join(module_path, 'data', fname)


def is_file_nfc(path):
    """

    Args:
        path: File path

    Returns: True if file is valid nfc and False if not. Raises a ValueError if path is not correct

    """
    text = open(path).read()
    return is_text_nfc(text)


def is_text_nfc(text):
    """Validate unicode form of given text"""
    nfc_text = "".join(c for c in unicodedata.normalize("NFC", text))
    if nfc_text == text:
        return True
    else:
        return False


def string_to_path(string):
    return Path(string)


def file_info(filename):
    """File metadata useful for various ADR tasks"""

    print("\nFilename: " + filename)
    print("---------------------------------")

    lines = tuple(open(filename, "r", encoding="utf-8"))
    num_utts = len(lines)

    text = "".join(
        c for c in unicodedata.normalize("NFC", open(filename, encoding="utf-8").read())
    )
    words = re.findall("\w+", text)
    num_words = len(words)
    num_chars = len(re.findall(r"\S", text))

    unique_chars = set(text)
    num_uniq_chars = len(unique_chars)

    print(sorted(unique_chars))
    print("# utts      : " + str(num_utts))
    print("# chars     : " + str(num_chars))
    print("# uniq chars: " + str(num_uniq_chars))

    # unaccented word stats
    unaccented_words = 0
    for word in words:
        if word == strip_accents_text(word):
            unaccented_words += 1

    print("# total words: " + str(num_words))
    print("# unaccented words : " + str(unaccented_words))
    print("-----------------------------------------------")

    # ambiguous word stats
    ambiguity_map = defaultdict(set)
    for word in words:
        no_accents = strip_accents_text(word)
        ambiguity_map[no_accents].add(word)

    ambiguous_words = 0
    ambiguous_words_2 = 0
    ambiguous_words_3 = 0
    ambiguous_words_4 = 0
    ambiguous_words_5 = 0
    ambiguous_words_6 = 0
    ambiguous_words_7 = 0
    ambiguous_words_8 = 0
    ambiguous_words_9 = 0

    # fill ambiguity map
    for word in ambiguity_map:
        if len(ambiguity_map[word]) > 1:
            ambiguous_words += 1
        if len(ambiguity_map[word]) == 2:
            ambiguous_words_2 += 1
        elif len(ambiguity_map[word]) == 3:
            ambiguous_words_3 += 1
        elif len(ambiguity_map[word]) == 4:
            ambiguous_words_4 += 1
        elif len(ambiguity_map[word]) == 5:
            ambiguous_words_5 += 1
        elif len(ambiguity_map[word]) == 6:
            ambiguous_words_6 += 1
        elif len(ambiguity_map[word]) == 7:
            ambiguous_words_7 += 1
        elif len(ambiguity_map[word]) == 8:
            ambiguous_words_8 += 1
        elif len(ambiguity_map[word]) == 9:
            ambiguous_words_9 += 1

    # print ambiguity map
    for word in ambiguity_map:
        if len(ambiguity_map[word]) == 2:
            print("# 2: " + str(ambiguity_map[word]))
        if len(ambiguity_map[word]) == 3:
            print("# 3: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 4:
            print("# 4: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 5:
            print("# 5: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 6:
            print("# 6: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 7:
            print("# 7: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 8:
            print("# 8: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 9:
            print("# 9: " + str(ambiguity_map[word]))

    print("# unique ambiguous words : " + str(ambiguous_words))
    print("# total unique non-diacritized words : " + str(len(ambiguity_map)))

    unique_all_words = set()
    for word in words:
        unique_all_words.add(word)

    print("# total unique words : " + str(len(unique_all_words)))
    print("-----------------------------------------------")
    print("# ambiguous 2 words : " + str(ambiguous_words_2))
    print("# ambiguous 3 words : " + str(ambiguous_words_3))
    print("# ambiguous 4 words : " + str(ambiguous_words_4))
    print("# ambiguous 5 words : " + str(ambiguous_words_5))
    print("# ambiguous 6 words : " + str(ambiguous_words_6))
    print("# ambiguous 7 words : " + str(ambiguous_words_7))
    print("# ambiguous 8 words : " + str(ambiguous_words_8))
    print("# ambiguous 9 words : " + str(ambiguous_words_9))


def get_data_path():
    data_dir = "iranlowo-data"
    path = os.getenv('IRANLOWO_DATADIR', os.path.join("~", data_dir))
    path = os.path.expanduser(path)
    os.makedirs(path, exist_ok=True)
    return path


