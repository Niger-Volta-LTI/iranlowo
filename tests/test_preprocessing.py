import os

from iranlowo import preprocessing


def test_is_valid_owe_format():
    cwd = os.getcwd()
    fail_path = cwd + "/tests/testdata/nfc.txt"
    pass_path = cwd + "/tests/testdata/owe_pass.txt"

    assert preprocessing.is_valid_owé_format(fail_path) is False
    assert preprocessing.is_valid_owé_format(pass_path) is True


def test_convert_to_owé_format():
    "Not exactly sure how to test this yet."
    assert True is True
