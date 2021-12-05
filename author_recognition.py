import numpy as np

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
        self.alphabet = list(get_alphabet_of_multiple_texts([item for sublist in cleaned_texts for item in sublist]))
        
        for author_texts, author_name in zip(cleaned_texts, author_names):
            author = Author(author_name)
            for text in author_texts:
                transition_matrix = compute_transition_matrix_2d(text, self.alphabet)
                author.add_transition_matrix(transition_matrix)
            self.authors.append(author)
        
    def predict(self, text_names):
        return_list = []
        for text_name in text_names: 
            text = get_cleaned_text_from_file(text_name) #cleaned
            log_probas = [calculate_probability_2d(text, self.alphabet, author.T) for author in self.authors]
            index = np.argmax(log_probas)
            return_list.append(self.authors[index].name)
        return return_list

    def clean(self, text_names):
        return list(map(lambda author_texts: list(map(lambda text_name: get_cleaned_text_from_file(text_name), author_texts)), text_names))


classifier = AuthorClassifier()
classifier.train([["Strugacki1.txt"], ["Dostoevsky1.txt"], ["Bulgakov1.txt"]], ["Братья Стругацкие", "Достоевский", "Булгаков"])
print(classifier.predict(["Bulgakov2.txt"]))