import numpy as np
from numpy import log

import nltk
from nltk import word_tokenize
from nltk import RegexpTokenizer
from nltk import ngrams

import string

def log0(x):
    return 0 if x <= 0 else log(x)

def getRidOfUpperCase(tokens): 
    return ([w.lower() for w in tokens])

def getTransitionMatrixFromFile(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokens = tokenizer.tokenize(file.read().replace('\n', ' '))
        cleaned_tokens = getRidOfUpperCase(tokens)
        print(cleaned_tokens)
        return computeTransitionMatrix(cleaned_tokens)

getTransitionMatrixFromFile("Strugacki1.txt")

