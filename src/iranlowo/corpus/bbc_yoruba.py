from iranlowo.corpus import Corpus


class BBCCorpus(Corpus):
    def __init__(self, path):
        """

        Args:
            path:
        """
        super(BBCCorpus, self).__init__(path=self.path, **kwargs)
        super().__init__(path)

