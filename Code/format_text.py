import sys
from re import split, sub, IGNORECASE

def load_text(filename):
    '''Reads file data, converts all words to lowercase, strips starting & trailing punctuation and splits words into a list'''
    with open(filename, 'r') as f:
        read_data = f.read()
    return read_data    
        
def cleanup_text(corpus):
    corpus = corpus.lower()
    strip_punc = sub('([\-\()"]*)([a-z]+)([?:!.,;\-\)"]*)',r'\2', corpus)
    words = split(r'\s', strip_punc)
    return words

def add_start(text):
    '''Adds an start signaler to last word'''
    text.insert(0, '<START>')
    return text

def add_stop(text):
    '''Adds an end stop signaler to last word'''
    text.append('<STOP>')
    return text

def structure_sentence(text):
    cap = " ".join(text).capitalize()
    sentence = f"{cap}."
    return sentence