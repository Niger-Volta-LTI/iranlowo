import gzip
import os

import yaml
from gensim import interfaces
from gensim.corpora.csvcorpus import CsvCorpus
from gensim.corpora.textcorpus import walk

from iranlowo.preprocessing import is_valid_owé_format, normalize_diacritics_text
from iranlowo.utils import is_text_nfc


class Corpus(interfaces.CorpusABC):
    def __init__(
        self,
        path=None,
        text=None,
        stream=False,
        fformat="txt",
        cformat=None,
        labels=False,
        preprocess=None,
    ):
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
        assert (
            self.path or self.text
        ), "You should pass either a path or text to read data from."
        if not self.preprocess:
            self.preprocess = [normalize_diacritics_text]
        self.data = (
            self.read_file_filename_or_text(text=text)
            if text
            else self.read_file_filename_or_text()
        )
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
                text = self.read_file_filename_or_text(f)
                out.append(text)
            return out
        else:
            if isinstance(path, str):
                if self.fformat == "txt":
                    text = open(path)
                elif self.fformat == "csv":
                    text = CsvCorpus(path, self.labels)
                elif self.fformat == "gzip":
                    text = gzip.open(path)
            else:
                text = self.path.seek(0)

            text = (
                text.read() if not self.stream else "".join(list(self.streamfile(text)))
            )
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
            data = "".join(data)
        if not self.cformat and not is_text_nfc(data):
            raise TypeError("The corpus does not comply to the NFC corpus format")
        elif self.cformat == "owe":
            if not is_valid_owé_format(data):
                raise TypeError(
                    "The corpus does not comply to the {0} corpus format".format(
                        self.cformat
                    )
                )
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
        self.dir_path = path
        self.depth = kwargs.get("min_depth", 0)
        self.path = list(self.read_files())
        super(DirectoryCorpus, self).__init__(path=self.path, **kwargs)

    def read_files(self):
        walked = list(walk(self.dir_path))
        if not walked:
            raise NotADirectoryError(
                "'{}' is not a valid directory".format(self.dir_path)
            )
        for depth, dirpath, _, filenames in walked:
            if self.depth <= depth:
                for path in filenames:
                    yield os.path.join(dirpath, path)


def get_corpus(name, niger_volta=False, **kwargs):
    def file_or_dir(path, mode):
        if mode == "single":
            return Corpus(path=path, **kwargs)
        else:
            return DirectoryCorpus(path=path, **kwargs)

    print(os.environ.get('NIGER_VOLTA_CORPUS'))
    print(os.environ.get('TEST_DIR'))
    with open(os.path.join(os.path.dirname(__file__), "corpus.yml"), "r") as stream:
        data = yaml.safe_load(stream)
    if niger_volta:
        nvc = data.get("niger_volta")
        if name not in nvc.keys():
            raise ValueError("Corpus {} does not exist".format(name))
        else:
            if not os.environ.get("NIGER_VOLTA_CORPUS", None):
                raise NotADirectoryError(
                    "NIGER_VOLTA_CORPUS environment variable not found. Please, clone the corpus repository from https://github.com/Niger-Volta-LTI/yoruba-text and set to NIGER_VOLTA_CORPUS to it's "
                    "path"
                )
            path = os.path.join(os.environ["NIGER_VOLTA_CORPUS"], nvc[name]["path"])
            return file_or_dir(path, nvc[name]["mode"])
    else:
        if name not in data.keys():
            raise ValueError("Corpus {} does not exist".format(name))
        path = os.path.join(
            os.path.dirname(__file__), "{}".format(data[name]["path"])
        )
        return file_or_dir(path, data[name]["mode"])


def get_corpus_path(name):
    with open(os.path.join(os.path.dirname(__file__), "corpus.yml"), "r") as stream:
        data = yaml.safe_load(stream)
        if name not in data.keys():
            raise ValueError("Corpus {} does not exist".format(name))
        else:
            return os.path.join(os.path.dirname(__file__), data[name])


def download_corpus(name, uri=None):
    pass
