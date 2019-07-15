import string
import unittest
from pathlib import Path

from iranlowo import corpus
from tests.utils import datapath


class TestTextCorpus(unittest.TestCase):
    def setUp(self):
        self.corpus_class = corpus.Corpus
        self.directory_loader = corpus.DirectoryCorpus
        self.txt_extension = 'txt'
        self.csv_extension = 'csv'
        self.gzip_extension = 'gzip'

    def test_load_corpus_from_path(self):
        path = datapath('owe_pass')
        corpus = self.corpus_class(path=path, fformat=self.txt_extension)
        self.assertEqual(len(corpus), 420)

    def test_load_corpus_from_path_stream(self):
        path = datapath('owe_pass')
        corpus = self.corpus_class(path=path, fformat=self.txt_extension, stream=True)
        self.assertEqual(len(corpus), 420)

    def test_load_corpus_from_text(self):
        text = open(datapath('owe_pass')).read()
        corpus = self.corpus_class(text=text)
        self.assertEqual(len(corpus), 420)

    def test_load_corpus_with_preprocessing(self):
        lines = [
            "Àwọn obìnrin, wọn ní kiní agbára yẹn lórí àwọn ọkùnrin?",
            "Ati gbọ́ọ rí daadaa mà, báwo ni ẹ ṣe maa ri, mà?",
            "eranko wo lo buru julo"
        ]
        expected = [
            'Àwọn obìnrin wọn ní kiní agbára yẹn lórí àwọn ọkùnrin',
            "ati gbọ́ọ rí daadaa mà, báwo ni ẹ ṣe maa ri, mà?",
            'erankowoloburujulo'
        ]

        def punctuations(text): return text.translate(str.maketrans('', '', string.punctuation))

        preprocessing = [
            lambda x: punctuations(x), lambda x: x.lower(), lambda x: x.replace(' ', '')
        ]

        for index, entry in enumerate(lines):
            corpus = self.corpus_class(text=entry, preprocess=preprocessing[index])
            self.assertEqual(corpus.data, expected[index])

    def test_load_corpus_from_directory(self):
        direc = datapath('dirdata')
        invalid_dir = datapath('test_data')
        multi_dir = datapath()
        path = Path(direc).glob('*')
        dir_corpus = self.directory_loader(path=direc)
        self.assertEqual(len(dir_corpus.data), len(list(path)))
        with self.assertRaises(NotADirectoryError):
            self.directory_loader(path=invalid_dir)
        multi_corp = self.directory_loader(path=multi_dir)
        multi_path = Path(multi_dir).glob('**/*')
        self.assertEqual(len(multi_corp.data), len(list(multi_path))-1)

    def test_save(self):
        pass

