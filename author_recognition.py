import numpy as np
from numpy import log

import nltk
from nltk import word_tokenize
from nltk import ngrams

import string

def log0(x):
    return 0 if x <= 0 else log(x)

def getTransitionMatrixFromFile(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        text = word_tokenize(file.read().replace('\n', ' '))
        cleaned_text = getRidOfPunctuationAndUpperWords(text)

        return computeTransitionMatrix(cleaned_text)