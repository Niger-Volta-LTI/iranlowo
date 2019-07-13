from iranlowo.corpus import Corpus


class BibeliCorpus(Corpus):
    def __init__(self, path):
        """

        Args:
            path:
        """
        super(BibeliCorpus, self).__init__(path=self.path, **kwargs)

