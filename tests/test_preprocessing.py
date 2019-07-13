import os
import unittest

from iranlowo import preprocessing
from tests.utils import datapath


class IranlowoCorpusTest(unittest.TestCase):

    def test_is_valid_owe_format(self):
        fail_path = datapath('nfc.txt')
        self.assertFalse(preprocessing.is_valid_owé_format(fail_path))
