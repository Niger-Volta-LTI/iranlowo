import gensim


class Tokenizer(object):
    def __init__(self, text, model=None, symbol=' ', func=None):
        """

        Args:
            text:
            model:
            symbol:
            func:
        """
        self.text = text
        self.symbol = symbol
        self.func = func
        self.model = model

    def ngram_tokenize(self):
        pass

    def word_tokenize(self, symbol=None, map_entities=False):
        if map_entities:
            email, num, link, abb = "<EMAIL>", "<NUM>", "<LINK>", "<ABB>"
        if not symbol:
            tokens = gensim.utils.simple_tokenize(self.text)
        else:
            tokens = [x for x in self.text]

    def sentence_tokenize(self, min_words_to_split=10, min_words_in_utt=5):
        output = []
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

    def morph_tokenize(self):
        pass
