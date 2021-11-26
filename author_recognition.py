import numpy as np
from numpy import log

import nltk
from nltk import word_tokenize
from nltk import RegexpTokenizer
from nltk import ngrams

import string

from author import Author

class AuthorClassifier:
    def train(texts, authors):
        pass
    def predict(texts):
        pass

def log0(x):
    return 0 if x <= 0 else log(x)

def getAlphabet(text):
    return list(set(text))

def computeTransitionMatrix(text):
    alphabet = getAlphabet(text)
    print(alphabet)

    T = np.zeros([SYMBOLS,SYMBOLS])
    bigrams = ngrams(text, 2)
    for bigram in bigrams:
        first = bigram[0]
        second = bigram[1]
        T[LetterIndices.index(first), LetterIndices.index(second)] += 1

    sums = np.sum(T, axis=1)

    for i in range(SYMBOLS):
        if sums[i] != 0:
            T[i,:]/=sums[i]
    return T

def getRidOfUpperCase(tokens): 
    return ([w.lower() for w in tokens])


def getTransitionMatrixFromFile(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokens = tokenizer.tokenize(file.read().replace('\n', ' '))
        cleaned_tokens = getRidOfUpperCase(tokens)

        cleaned_text = " ".join(cleaned_tokens)
        return computeTransitionMatrix(cleaned_text)

getTransitionMatrixFromFile("Strugacki1.txt")

