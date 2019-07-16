import unittest

from iranlowo import corpus


class TestCoprusLoader(unittest.TestCase):
    def setUp(self):
        self.owe_loader = corpus.OweLoader

    def test_load_owe(self):
        with self.assertRaises(NotADirectoryError):
            self.owe_loader()
