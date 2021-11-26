import nltk
from nltk import RegexpTokenizer

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
        #return computeTransitionMatrix2D(cleaned_text)
        return cleaned_text