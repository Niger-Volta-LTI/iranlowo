import gzip
import os
import sys


from gensim import interfaces
from gensim.corpora.csvcorpus import CsvCorpus
from gensim.corpora.textcorpus import walk

from iranlowo.preprocessing import is_valid_owé_format, normalize_diacritics_text
from iranlowo.utils import is_text_nfc


class Corpus(interfaces.CorpusABC):
    def __init__(self, path=None, text=None, stream=False, fformat='txt', cformat=None, labels=False, preprocess=None):
        """

        Args:
            path:
            text:
        """
        self.path = path
        self.text = text
        self.labels = labels
        self.stream = stream
        self.fformat = fformat
        self.cformat = cformat
        self.preprocess = preprocess
        if not self.preprocess:
            self.preprocess = [normalize_diacritics_text]
        self.data = self.read_file_filename_or_text(text=text) if text else self.read_file_filename_or_text()
        self.validate_format()

    def __iter__(self):
        for line in self.data:
            yield line

    def __len__(self):
        return len(self.data)

    @staticmethod
    def save_corpus(fname, corpus, id2word=None, metadata=False):
        pass

    def streamfile(self, fobj):
        num_text = 0
        with fobj as obj:
            for line in obj:
                num_text += 1
                yield line

    def read_file_filename_or_text(self, f=None, text=None):
        """

        Returns:

        """
        path = f if f else self.path
        out = []
        if text:
            return self.handle_preprocessing(text) if self.preprocess else text
        elif isinstance(path, list):
            for f in path:
                path.remove(f)
                sys.setrecursionlimit(10000)
                text = self.read_file_filename_or_text(f)
                out.append(text)
        else:
            if isinstance(path, str):
                if self.fformat == "txt":
                    text = open(path)
                elif self.fformat == "csv":
                    text = CsvCorpus(path, self.labels)
                elif self.fformat == 'gzip':
                    text = gzip.open(path)
            else:
                text = self.path.seek(0)

            text = text.read() if not self.stream else ''.join(list(self.streamfile(text)))
            return self.handle_preprocessing(text) if self.preprocess else text

    def handle_preprocessing(self, text):
        if callable(self.preprocess):
            return self.preprocess(text)
        if isinstance(self.preprocess, list):
            for technique in self.preprocess:
                text = technique(text)
            return text

    def validate_format(self):
        """

        Returns:

        """
        data = self.data
        if isinstance(data, list):
            data = ''.join(data)
        if not self.cformat and not is_text_nfc(data):
            raise TypeError("The corpus does not comply to the NFC corpus format")
        elif self.cformat == "owe":
            if not is_valid_owé_format(data):
                raise TypeError("The corpus does not comply to the {0} corpus format".format(self.cformat))
            else:
                return True

    def generate(self, size):
        """

        Args:
            size:

        Returns:

        """
        if not self.cformat:
            raise ValueError("You need to specify a format for generating random text")


class DirectoryCorpus(Corpus):
    def __init__(self, path, **kwargs):
        self.path_dir = path
        walked = list(walk(self.path_dir))
        self.depth = walked[0][0]
        self.dirnames = walked[0][2]
        self.flist = walked[0][3]
        self.path = list(self.read_files())
        super(DirectoryCorpus, self).__init__(path=self.path, **kwargs)

    def read_files(self):
        for path in self.flist:
            yield os.path.join(self.path_dir, path)
