import numpy as np
from numpy import log

import nltk
from nltk import ngrams

import string

from author import *
from author_auxiliary import *


class AuthorClassifier:
    def train(texts, author_names):
        #на вход ([[], []], []) : у каждого автора может быть несколько текстов
        for author_texts, author_name in zip(texts, author_names):
            author = Author(author_name)
    def predict(texts):
        pass


cleaned = getCleanedTextFromFile("Strugacki1.txt")
print(computeTransitionMatrix2D(cleaned, list(getAlphabetOfMultipleTexts([cleaned]))))