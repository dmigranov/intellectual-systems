def getAlphabet(text):
    return set(text)

def getAlphabetOfMultipleTexts(texts):
    alphabets = [getAlphabet(text) for text in texts]
    common_alphabet = set.union(*alphabets) 
    return common_alphabet
    