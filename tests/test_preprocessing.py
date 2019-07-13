import os
import unittest

from iranlowo import preprocessing


class IranlowoCorpusTest(unittest.TestCase):

    def test_is_valid_owe_format(self):
        cwd = os.getcwd()
        fail_path = cwd + "/tests/testdata/nfc.txt"

        assert preprocessing.is_valid_owé_format(fail_path) is False
