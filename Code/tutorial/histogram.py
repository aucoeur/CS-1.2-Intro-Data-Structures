import sys
from re import split, sub, IGNORECASE
from utils import time_it

@time_it
def load_text(filename):
    '''Reads file data, converts all words to lowercase, strips trailing punctuation and splits words into a list'''
    with open(filename, 'r') as f:
        read_data = f.read().lower()
        strip_punc = sub('([a-z]+)[?:!.,;]*',r'\1', read_data)
        words = split(r'\s', strip_punc)
    return words

@time_it
def histogram(source_text):
    '''Turns source_text into dictionary with word counts'''

    histo = {}
    for word in source_text:
        # No .append() for dict. To add new key to dict, use assignment operator with dict key.
        histo[word] = histo.get(word, 0) + 1

    return histo

@time_it
def listogram(source_text):
    '''Turns source_text into lists in a list with word counts'''

    histo = []
    new_word = True
    for word in source_text:
        for item in histo:
            if item[0] == word:
                item[1] += 1
                new_word = False 
        if new_word:
            histo.append([word, 1])

    return histo

@time_it
def tuplogram(source_text):
    '''Turns source_text into tuples in a list with word counts'''

    histo = []
    new_word = True
    for word in source_text:
        for index, item in enumerate(histo):
            if item[0] == word:
                histo[index] = (word, (item[1] + 1))
                break
        if new_word:
            histo.append((word, 1))

    return histo

# Stas' Zip method
# def tuple_histogram(source_text):
#     histogram = []
#     word_frequencies = []
#     add_word = True
#     for word in source_text:
#         if word not in histogram:
#             histogram.append(word)
#             word_frequencies.append(1)
#         else:
#             word_index = histogram.index(word)
#             word_frequencies[word_index] += 1
#     tuple_list = zip(histogram, word_frequencies)
#     tuple_list = list(tuple_list)
#     return tuple_list

@time_it
def countogram(source_text):
    '''Turns source_text into list sorted by number of appearances'''

    histo = histogram(source_text)
    count_dict = {}

    for key, value in histo.items():
        count_dict.setdefault(value, []).append(key)

    return sorted(count_dict.items(), reverse=True)
        
def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram.get(word, 'Key doesn\'t exist')

def sort(histogram):
    sort_histo = sorted(histogram.items(), key = lambda item: item[1], reverse=True)
    return sort_histo

if __name__ == "__main__":
    text = 'sample_text.txt'
    # text = 'islandofdrmoreau.txt'
    source_text = load_text(text)
    histo = histogram(source_text)
    # listo = listogram(source_text)
    # tuplo = tuplogram(source_text)
    print(countogram(source_text))
    # print(histo)
    # print(listo)
    # print(tuplo)
    # print(unique_words(histo))
    # print(frequency('sugar', histo))
    # for each in sort(histo):
        # print(f"{each[0]}: {each[1]}")
    # print(sort(histo))