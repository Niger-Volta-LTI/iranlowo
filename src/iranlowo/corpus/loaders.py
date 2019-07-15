import os

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
        super(YorubaBlogCorpus, self).__init__(path=self.path, **kwargs)


class BBCCorpus(Corpus):
    def __init__(self, path):
        """

        Args:
            path:
        """
        super(BBCCorpus, self).__init__(path=self.path, **kwargs)
        super().__init__(path)


class BibeliCorpus(Corpus):
    def __init__(self, path):
        """

        Args:
            path:
        """
        super(BibeliCorpus, self).__init__(path=self.path, **kwargs)


class en(BaseLoader, DirectoryCorpus):
    def __init__(self):
        BaseLoader.__init__(self, corpus_path="Owe/en")
        DirectoryCorpus.__init__(self, path=self.path)


class yo(BaseLoader, DirectoryCorpus):
    def __init__(self):
        BaseLoader.__init__(self, corpus_path="Owe/yo")
        DirectoryCorpus.__init__(self, path=self.path)


class OweLoader(object):
    def __init__(self):
        self.en = en()
        self.yo = yo()

