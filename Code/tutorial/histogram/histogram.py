import sys
from re import split, sub, IGNORECASE

def load_text(filename):
    '''Reads file data and strips trailing punctuation and splits words into a list'''
    with open(filename, 'r') as f:
        read_data = f.read().lower()
        strip_punc = sub('([a-z]+)[?:!.,;]*',r'\1', read_data)
        words = split(r'\s', strip_punc)
    return words

def histogram(source_text) -> dict:
    '''Turns source_text into dictionary with word counts'''
    histo = {}
    for word in source_text:
        histo[word] = histo.get(word, 0) + 1
    return histo

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]

if __name__ == "__main__":
    text = 'sample_text.txt'
    source_text = load_text(text)
    histo = histogram(source_text)
    print(histo)
    print(unique_words(histo))
    print(frequency('sugar', histo))