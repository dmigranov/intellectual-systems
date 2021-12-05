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
        alphabet = list(get_alphabet_of_multiple_texts([item for sublist in cleaned_texts for item in sublist]))
        
        for author_texts, author_name in zip(cleaned_texts, author_names):
            author = Author(author_name)
            for text in author_texts:
                transition_matrix = compute_transition_matrix_2d(text, alphabet)
                author.add_transition_matrix(transition_matrix)
            self.authors.append(author)
        
    def predict(self, text_names):
        return_list = []
        for text_name in text_names: 
            text = get_cleaned_text_from_file(text_name) #cleaned
            probas = [calculate_probability_2d(text, author.T) for author in self.authors]
            probas_softmax = softmax(probas)
            print(probas_softmax)

            

    def clean(self, text_names):
        return list(map(lambda author_texts: list(map(lambda text_name: get_cleaned_text_from_file(text_name), author_texts)), text_names))


cleaned = get_cleaned_text_from_file("Strugacki1.txt")
print(compute_transition_matrix_2d(cleaned, list(get_alphabet_of_multiple_texts([cleaned]))))

classifier = AuthorClassifier()
classifier.train([["Strugacki1.txt", "Dostoevsky1.txt"]], ["Братья Стругацкие, Достоевский"])
classifier.predict(["Strugacki1.txt"])