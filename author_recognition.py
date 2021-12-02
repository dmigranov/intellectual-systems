import numpy as np
from numpy import log

import nltk
from nltk import ngrams

import string

from author import *
from author_auxiliary import *


class AuthorClassifier:
    def __init__(self):
        self.authors = []

    def train(self, text_names, author_names):
        #на вход ([[], []], []) : у каждого автора может быть несколько текстов
        cleaned_texts = self.clean(text_names)
        alphabet = list(getAlphabetOfMultipleTexts([item for sublist in cleaned_texts for item in sublist]))
        
        for author_texts, author_name in zip(cleaned_texts, author_names):
            author = Author(author_name)
            for text in author_texts:
                transition_matrix = computeTransitionMatrix2D(text, alphabet)
                author.add_transition_matrix(transition_matrix)
            self.authors.append(author)
        
    def predict(self, texts):
        pass

    def clean(self, text_names):
        return list(map(lambda author_texts: list(map(lambda text_name: getCleanedTextFromFile(text_name), author_texts)), text_names))


cleaned = getCleanedTextFromFile("Strugacki1.txt")
print(computeTransitionMatrix2D(cleaned, list(getAlphabetOfMultipleTexts([cleaned]))))

classifier = AuthorClassifier()
classifier.train([["Strugacki1.txt", "Dostoevsky1.txt"]], ["Братья Стругацкие, Достоевский"])