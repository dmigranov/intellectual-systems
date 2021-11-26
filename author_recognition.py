import numpy as np
from numpy import log

import nltk
from nltk import word_tokenize
from nltk import ngrams

import string

def log0(x):
    return 0 if x <= 0 else log(x)

    
    