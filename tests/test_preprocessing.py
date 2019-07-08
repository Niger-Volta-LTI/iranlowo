import os

from iranlowo import preprocessing


def test_is_valid_owe_format():
    cwd = os.getcwd()
    fail_path = cwd + "/tests/testdata/nfc.txt"

    assert preprocessing.is_valid_owé_format(fail_path) is False
