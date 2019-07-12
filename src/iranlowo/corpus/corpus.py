import gzip
import os
import sys

import requests

from gensim import interfaces
from gensim.corpora.csvcorpus import CsvCorpus
from gensim.corpora.textcorpus import lower_to_unicode, strip_multiple_whitespaces, walk
from gensim.utils import deaccent

from iranlowo.preprocessing import is_valid_owé_format
from iranlowo.utils import is_text_nfc


class Corpus(interfaces.CorpusABC):
    def __init__(self, path=None, text=None, is_url=False, rlist=False, stream=False, fformat='txt', cformat=None, labels=False, preprocess=False):
        """

        Args:
            path:
            text:
            **kwargs:
        """
        self.path = path
        self.text = text
        self.rlist = rlist
        self.labels = labels
        self.stream = stream
        self.fformat = fformat
        self.preprocess = preprocess
        self.cformat = cformat
        self.is_url = is_url
        self.data = text if text else self.read_file_or_filename()
        self.validate_format()

    def __iter__(self):
        for line in self.data:
            yield line

    def __len__(self):
        return len(self.data)

    def get_data(self):
        pass

    @staticmethod
    def save_corpus(fname, corpus, id2word=None, metadata=False):
        pass

    def streamfile(self, fobj):
        num_text = 0
        with fobj as obj:
            for line in obj:
                num_text += 1
                yield line

    def read_file_or_filename(self, f=None):
        """

        Returns:

        """
        path = f if f else self.path
        text = None
        print(len(self.path))
        out = []
        if isinstance(path, list):
            for f in path:
                path.remove(f)
                sys.setrecursionlimit(10000)
                text = self.read_file_or_filename(f)
                out.append(text)
        else:
            if self.is_url:
                r = requests.get(path)
                if r.status_code in [200, 201]:
                    text = r.text
                    return text
            elif isinstance(path, str):
                if self.fformat == "txt":
                    text = open(path)
                elif self.fformat == "csv":
                    text = CsvCorpus(path, self.labels)
                elif self.fformat == 'gzip':
                    text = gzip.open(path)
            else:
                text = self.path.seek(0)

            if not self.stream:
                text = text.read() if not self.rlist else text.readlines()
                print(text)
                if self.preprocess:
                    text = self.handle_preprocessing(text)
                return text
            else:
                self.streamfile(text)

    def handle_preprocessing(self, text):
        if callable(self.preprocess):
            return self.preprocess(text)
        if isinstance(self.preprocess, list):
            prep_list = self.preprocess if isinstance(self.preprocess, list) else [lower_to_unicode, deaccent, strip_multiple_whitespaces]
            for technique in prep_list:
                text = technique(self.data)
            return text

    def validate_format(self):
        """

        Returns:

        """
        data = self.data
        if isinstance(data, list):
            data = ' '.join(data)
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

