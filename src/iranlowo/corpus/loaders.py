import os

from iranlowo.corpus import get_corpus

os.environ[
    "NIGER_VOLTA_CORPUS"
] = "/Users/Olamilekan/Desktop/Machine Learning/OpenSource/yoruba-text"


def niger_volta_corpus(corpus_code):
    return get_corpus(name=corpus_code, niger_volta=True)
