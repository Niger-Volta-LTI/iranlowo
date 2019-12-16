import unittest
import os
from iranlowo.corpus import loaders, corpus


class TestCoprusLoader(unittest.TestCase):
    def test_load_yoruba_blog(self):
        yb = loaders.niger_volta_corpus('yoruba_blog')
        self.assertIsInstance(yb, corpus.Corpus)

    def test_load_owe_empty(self):
        with self.assertRaises(NotADirectoryError):
            loaders.niger_volta_corpus('owe_yoruba')

    def test_load_corpus_does_not_exist(self):
        with self.assertRaises(ValueError):
            loaders.niger_volta_corpus('owe')

    def test_load_normal_corpus(self):
        syllables = corpus.get_corpus('syllables')
        self.assertIsInstance(syllables, corpus.Corpus)
