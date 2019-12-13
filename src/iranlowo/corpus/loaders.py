import os
from ruamel.yaml import YAML
from pathlib import Path

from iranlowo.corpus import Corpus, DirectoryCorpus


class BaseLoader(object):
    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        yoruba_text_path = os.environ.get("YORUBA_TEXT_PATH", None)
        if not yoruba_text_path:
            raise NotADirectoryError(
                "YORUBA_TEXT_PATH environment variable not found. Please, clone the corpus repository from https://github.com/Niger-Volta-LTI/yoruba-text and set to YORUBA_TEXT_PATH to it's "
                "path")
        else:
            corpus_path = "{}/{}".format(yoruba_text_path, corpus_path)
            self.path = corpus_path


class YorubaBlogCorpus(Corpus):
    def __init__(self, path):
        """

        Args:
            path:
        """
        super(YorubaBlogCorpus, self).__init__(path=self.path)


class BBCCorpus(Corpus):
    def __init__(self, path):
        """

        Args:
            path:
        """
        super(BBCCorpus, self).__init__(path=self.path)


class BibeliCorpus(Corpus):
    def __init__(self, path):
        """

        Args:
            path:
        """
        super(BibeliCorpus, self).__init__(path=self.path)


class en(BaseLoader, DirectoryCorpus):
    def __init__(self):
        BaseLoader.__init__(self, corpus_path="Owe/en")
        DirectoryCorpus.__init__(self, path=self.path, cformat='owe')


class yo(BaseLoader, DirectoryCorpus):
    def __init__(self):
        BaseLoader.__init__(self, corpus_path="Owe/yo")
        DirectoryCorpus.__init__(self, path=self.path, cformat='owe')


class OweLoader(object):
    def __init__(self):
        self.en = en()
        self.yo = yo()


def get_corpus(name, single=False):
    yaml = YAML(typ='safe')
    data = yaml.load(Path('/Users/Olamilekan/Desktop/Machine Learning/OpenSource/iranlowo/src/iranlowo/corpus/corpus.yml'))
    if name not in data.keys():
        raise ValueError("Corpus {} does not exist".format(name))
    else:
        if not single:
            return Corpus(path=data[name]).data
        else:
            return DirectoryCorpus(path=data[name])


def get_corpus_path(name):
    yaml = YAML(typ='safe')
    data = yaml.load(Path('corpus.yml'))
    if name not in data.keys():
        raise ValueError("Corpus {} does not exist".format(name))
    else:
        return data['name']


def download(name):
    pass

