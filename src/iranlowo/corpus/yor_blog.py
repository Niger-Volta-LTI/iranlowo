from iranlowo.corpus import Corpus


class YorubaBlogCorpus(Corpus):
    def __init__(self, path):
        """

        Args:
            path:
        """
        super(YorubaBlogCorpus, self).__init__(path=self.path, **kwargs)

