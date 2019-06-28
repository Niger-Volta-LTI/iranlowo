import nltk
# nltk.download()

from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

# text = "I need to write a program in NLTK that breaks a corpus (a large collection of txt files) into unigrams, bigrams, trigrams, fourgrams and fivegrams. I need to write a program in NLTK that breaks a corpus"
text = ' '.join(
    ["all the information [laughter]",
     "all the information again",
     "all the information all that",
     "all the information and would need",
     "all the information but",
     "all the information for you and",
     "all the information from the vehicle on",
     "all the information from you but",
     "all the information i gave you guys",
     "all the information i had",
     "all the information i have",
     "all the information i have on here",
     "all the information i your account",
     "all the information in",
     "all the information in for you",
     "all the information is correct",
     "all the information on it",
     "all the information on it i just",
     "all the information on the vehicle",
     "all the information so they know all you know what i mean",
     "all the information that i can",
     "all the information that i had",
     "all the information that they need and then",
     "all the information that you how",
     "all the information they you need he would have to give you",
     "all the information uh",
     "all the information when you get here",
     "all the information you know",
     "all the information you need",
     "all the information you need on it",
     "all the information you need will be on it",
     "all the instructions on how to"])

token = nltk.word_tokenize(text)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)
fourgrams = ngrams(token,4)
fivegrams = ngrams(token,5)

print(Counter(ngrams(token,5)))