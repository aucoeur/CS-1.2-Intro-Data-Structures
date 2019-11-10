import sys
from random import choice, randrange
from utils import time_it

@time_it
def load_words(filename):
    '''Reads txt file of words'''

    # with open('sample_words.txt', 'r') as f:
    with open(filename, 'r') as f:
        read_data = f.read().splitlines()
    return read_data

    #     all_lines = f.readlines()
    #     lines = []
    #     # for line in all_lines:
    #     #     lines.append(line.strip())
    #     lines = [line.strip() for line in all_lines]
    # return lines

@time_it
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
    filename = '/usr/share/dict/words'
    word_list = load_words(filename)
    number = sys.argv[1]
    make_sentence(word_list, number)