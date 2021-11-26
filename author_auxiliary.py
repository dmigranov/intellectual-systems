def log0(x):
    return 0 if x <= 0 else log(x)

def getAlphabet(text):
    return set(text)

def getAlphabetOfMultipleTexts(texts):
    alphabets = [getAlphabet(text) for text in texts]
    common_alphabet = set.union(*alphabets) 
    return common_alphabet
    