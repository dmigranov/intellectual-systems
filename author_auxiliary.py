import nltk
from nltk import RegexpTokenizer
from nltk import ngrams

import numpy as np


def log0(x):
    return 0 if x <= 0 else log(x)

def getAlphabet(text):
    return set(text)

def getAlphabetOfMultipleTexts(texts):
    alphabets = [getAlphabet(text) for text in texts]
    common_alphabet = set.union(*alphabets) 
    return common_alphabet
    
def getRidOfUpperCase(tokens): 
    return ([w.lower() for w in tokens])


def getCleanedTextFromFile(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokens = tokenizer.tokenize(file.read().replace('\n', ' '))
        cleaned_tokens = getRidOfUpperCase(tokens)

        cleaned_text = " ".join(cleaned_tokens)
        return cleaned_text

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

def calculate_probability(text, transition_matrix):
    pass