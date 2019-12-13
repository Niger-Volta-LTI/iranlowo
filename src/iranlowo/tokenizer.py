from functools import lru_cache

import gensim

from iranlowo.corpus.loaders import get_corpus
from iranlowo.data.small import contains


class Tokenizer(object):
    def __init__(self, text, model=None, symbol=None, map_entities=True):
        """

        Args:
            text: Text to tokenize
            model: If exists, model will be loaded and used for the tokenization
            symbol: Symbol to match.
            map_entities: Map entities from tokenization result.
        """
        self.text = text
        self.symbol = symbol
        self.map_entities = map_entities
        self.model = model

    @lru_cache(maxsize=None)
    def syllable_tokenize(self, chunk=None):
        def get_valid_syllable(syl, chunk_):
            if len(chunk_) > 4:
                raise ValueError("Yoruba has no syllable with more than 4 characters.")
            if len(chunk_) == 4:
                if contains(chunk_, "diagraph"):
                    return chunk_
            elif len(chunk_) == 3 and (contains(chunk_, "diagraph") or contains(chunk_, "consonants")):
                return chunk_
            elif len(chunk_) == 2:
                if contains(chunk_, "consonants") and contains(chunk_, "vowels"):
                    if contains(chunk_[0], "consonants"):
                        return chunk_
                    else:
                        return chunk_[::-1]
            elif len(chunk_) == 1:
                if contains(chunk_, "vowels") and syl[0] == chunk_:
                    return chunk_
            else:
                return False

        tokens = []
        words = chunk if chunk else self.word_tokenize()
        syllables = get_corpus('syllables')
        for word in words:  # Check if word exists in our syllable list. If it does, add it.
            if word in syllables:
                tokens.append(word)
            else:
                for chunk_index in range(1, 5):  # Create chunk list and validate each chunk.
                    current_chunks = [(word[i:i + chunk_index]) for i in range(0, len(word), chunk_index)]
                    for current_chunk in current_chunks:
                        valid_chunk = get_valid_syllable(word, current_chunk)
                        if valid_chunk:
                            tokens.append(valid_chunk)
        return sorted(set(tokens))

    def subword_tokenize(self):
        pass

    def word_tokenize(self):
        if not self.symbol:
            tokens = gensim.utils.simple_preprocess(self.text)
        else:
            tokens = [x for x in self.text.split(self.symbol)]

        return tokens

    def sentence_tokenize_simple(self, match='fullstop'):
        """

        Args:
            match: List : Should be one of fullstop, whitespace or newline

        Returns:

        """
        symbol_map = {"fullstop": ".", "whitespace": " ", "newline": "\n", "whitespace+newline": 'default'}
        if not symbol_map.get(match):
            return self.text.split()
        print(symbol_map.get(match))
        return self.text.split(symbol_map.get(match))

    def sentence_tokenize(self, min_words_to_split=10, min_words_in_utt=5):
        output = []
        self.symbol = '.' if not self.symbol else self.symbol
        for line in self.text.splitlines():
            if self.symbol in line:
                num_words = len(line.split())
                num_commas = line.count(self.symbol)
                curr_comma_position = line.index(self.symbol)
                num_words_ahead_of_curr_comma = len(line[0:curr_comma_position].split())

                curr_line = line
                while num_commas > 0:
                    if num_words < min_words_to_split:
                        # print(curr_line.strip())
                        output.append(curr_line)
                        break
                    if num_words >= min_words_to_split:
                        if (
                                num_words_ahead_of_curr_comma >= min_words_in_utt
                                and len(curr_line[curr_comma_position:].split())
                                >= min_words_in_utt
                        ):
                            output.append(curr_line[0:curr_comma_position] + "\n")

                            # update vars
                            curr_line = curr_line[curr_comma_position + 1:]
                            num_words = len(curr_line.split())
                            num_commas = num_commas - 1
                            if num_commas > 0:
                                curr_comma_position = curr_line.index(self.symbol)
                                num_words_ahead_of_curr_comma = len(
                                    curr_line[0:curr_comma_position].split()
                                )
                            else:
                                output.append(curr_line)
                        else:
                            # ignore too short comma (+= vs = on current comma position)
                            num_commas = num_commas - 1
                            if num_commas > 0:  # for say 3 commas
                                curr_comma_position += (
                                        curr_line[curr_comma_position + 1:].index(self.symbol)
                                        + 1
                                )
                                num_words_ahead_of_curr_comma = len(
                                    curr_line[0:curr_comma_position].split()
                                )
                            else:
                                output.append(curr_line)
                    else:
                        output.append(curr_line)
            else:
                output.append(line)
        return output
