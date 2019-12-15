from iranlowo.corpus import get_corpus


def niger_volta_corpus(corpus_code):
    return get_corpus(name=corpus_code, niger_volta=True)
