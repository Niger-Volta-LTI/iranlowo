import os

from iranlowo.corpus import get_corpus

os.environ['NIGER_VOLTA_CORPUS'] = "/Users/Olamilekan/Desktop/Machine Learning/OpenSource/yoruba-text"


def niger_volta_corpus(corpus_code):
    nvc_path = os.environ.get("NIGER_VOLTA_CORPUS", None)
    if not nvc_path:
        raise NotADirectoryError(
            "NIGER_VOLTA_CORPUS environment variable not found. Please, clone the corpus repository from https://github.com/Niger-Volta-LTI/yoruba-text and set to NIGER_VOLTA_CORPUS to it's "
            "path")
    else:
        return get_corpus(name=corpus_code, niger_volta=True)
