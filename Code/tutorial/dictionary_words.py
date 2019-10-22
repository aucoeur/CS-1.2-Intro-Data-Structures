import sys
import os
from random import choice

def load_words():
    '''Reads txt file of words'''

    # with open('sample_words.txt', 'r') as f:
    with open('/usr/share/dict/words', 'r') as f:
        read_data = f.read().splitlines()

    return read_data

def make_sentence(words_list, number):
    '''Makes sentence from word list'''

    sentence = []

    while len(sentence) != int(number):
        random_word = choice(words_list)
        if random_word not in sentence:
            sentence.append(random_word)

    sentence = " ".join(sentence).capitalize()
    print(f'{sentence}.')

if __name__ == "__main__":
    word_list = load_words()
    number = sys.argv[1]
    make_sentence(word_list, number)