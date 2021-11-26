import numpy as np
from numpy import log

import nltk
from nltk import ngrams

import string

from author import *
from author_auxiliary import *


class AuthorClassifier:
    def train(texts, authors):
        pass
    def predict(texts):
        pass



def computeTransitionMatrix2D(text, alphabet): #alphabet is a list
    symbol_count = len(alphabet)

    T = np.zeros([symbol_count, symbol_count])
    bigrams = ngrams(text, 2)
    for bigram in bigrams:
        first = bigram[0]
        second = bigram[1]
        T[alphabet.index(first), alphabet.index(second)] += 1

    sums = np.sum(T, axis=1)

    for i in range(symbol_count):
        if sums[i] != 0:
            T[i,:] /= sums[i]

    return T




getCleanedTextFromFile("Strugacki1.txt")

