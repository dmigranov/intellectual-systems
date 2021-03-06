import nltk
from nltk import RegexpTokenizer
from nltk import ngrams

import numpy as np


def log0(x):
    return 0 if x <= 0 else np.log(x)

def get_alphabet(text):
    return set(text)

def get_alphabet_of_multiple_texts(texts):
    alphabets = [get_alphabet(text) for text in texts]
    common_alphabet = set.union(*alphabets) 
    return sorted(common_alphabet)
    
def get_rid_of_upper_case(tokens): 
    return ([w.lower() for w in tokens])


def get_cleaned_text_from_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        #tokenizer = nltk.RegexpTokenizer(r"[^\W\d_]+") #\w включает цифры
        tokenizer = nltk.RegexpTokenizer(r"[а-яёА-ЯЁ]+")
        tokens = tokenizer.tokenize(file.read().replace('\n', ' '))
        cleaned_tokens = get_rid_of_upper_case(tokens)
        cleaned_text = " ".join(cleaned_tokens)
        return cleaned_text

def compute_transition_matrix_2d(text, alphabet): #alphabet is a list
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

def calculate_probability_2d(text, alphabet, transition_matrix):
    bigrams = ngrams(text, 2)
    s = 0
    for bigram in bigrams:
        first = bigram[0]
        second = bigram[1]
        #todo: проверка на налчиие символов
        try:
            p = transition_matrix[alphabet.index(first), alphabet.index(second)]
        except ValueError:
            p = 0
        s += log0(p)
    return s