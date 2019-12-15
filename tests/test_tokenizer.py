import string
import unittest
from pathlib import Path

from iranlowo import corpus
from iranlowo.tokenizer import Tokenizer
from tests.utils import datapath


class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.word_tokenize_text = "Àwọn obìnrin, wọn ní kiní agbára yẹn lórí àwọn ọkùnrin"
        self.sentence_tokenize_text = "ise wonyii lawujo yoruba gbogbo.elesin ati agbateru orisa naa.ati fifi opin si idokowo.fun igba die lati le.gege bi alaga egbe naa.eedi ko je ki aye.eranko wo "\
                                      "lo buru julo "

        self.tokenizer = Tokenizer
        self.corpus_class = corpus.Corpus
        self.directory_loader = corpus.DirectoryCorpus
        self.txt_extension = 'txt'
        self.csv_extension = 'csv'
        self.gzip_extension = 'gzip'

    def test_syllable_tokenizer(self):
        syllable_tokens = self.tokenizer(self.word_tokenize_text).syllable_tokenize()
        self.assertEqual(len(syllable_tokens), 24)

    def test_subword_tokenizer(self):
        pass

    def test_word_tokenizer(self):
        word_tokens = self.tokenizer(self.word_tokenize_text).word_tokenize()
        self.assertEqual(len(word_tokens), 10)

    def test_sentence_tokenize_simple(self):
        sentence_tokens = self.tokenizer(self.sentence_tokenize_text).sentence_tokenize_simple()
        self.assertEqual(len(sentence_tokens), 7)

    def test_sentence_tokenize(self):
        sentence_tokens = self.tokenizer(self.sentence_tokenize_text).sentence_tokenize()
        self.assertEqual(len(sentence_tokens), 6)

