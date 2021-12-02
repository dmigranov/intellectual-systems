import numpy as np
from numpy import log

import nltk
from nltk import ngrams

import string

from author import *
from author_auxiliary import *


class AuthorClassifier:
    def train(self, texts, author_names):
        #на вход ([[], []], []) : у каждого автора может быть несколько текстов
        cleaned_texts = sefl.clean(texts)
        
        for author_texts, author_name in zip(texts, author_names):
            author = Author(author_name)
            for text in author_texts:
                cleaned_text = getCleanedTextFromFile("Strugacki1.txt")
                author.add_transition_matrix()
    def predict(self, texts):
        pass

    def clean(self, texts):
        return list(map(lambda author_texts: list(map(lambda text: getCleanedTextFromFile(text), author_texts)), texts))


cleaned = getCleanedTextFromFile("Strugacki1.txt")
#print(computeTransitionMatrix2D(cleaned, list(getAlphabetOfMultipleTexts([cleaned]))))

classifier = AuthorClassifier()
print(classifier.clean([["Strugacki1.txt"]]))