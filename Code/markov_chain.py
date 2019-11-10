from random import randint, randrange, choice
from format_text import load_text, cleanup_text, add_stop
from dictogram import Dictogram
from utils import time_it

@time_it
def find_pairs(corpus):
    '''Creates word pairs and puts them into a states dictionary'''

    pairs = []

    for i in range(len(corpus)-2):
        pairs.append((corpus[i], corpus[i+1]))
    
    markov_dict = {}

    for first, second in pairs:
        if first in markov_dict.keys():
            markov_dict[first].append(second)
        else:
            markov_dict[first] = [second]
    return markov_dict

@time_it
def markov_histo(markov_dict):
    '''Creates histogram from markov dict'''
 
    for key, value in markov_dict.items():
        markov_dict[key] = Dictogram(value)
    return markov_dict

@time_it
def stochastic_sample(markov, word):
    '''Gets a weighted random word from given word's histo'''
    histo = markov.get(word, 'NOPE')
    
    if word in markov:
        return histo.sample()
 
# def random_word(markov, word):
#     '''Takes given word and returns a random word in its markov list'''
#     total_links = len(markov[word])
#     if total_links >= 2:
#         random = randint(0, total_links-1) #janky fix to avoid picking last word
#         if total_links == 1:
#             random = randint(0, 1)
#         chain = markov[word][random]
#     else:
#         chain = markov[word][0]
#     return chain

@time_it
def random_walk(word, markov, steps):
    '''Given a starting word, picks a random word from markov list and walks to given number of steps to generate a sentence'''

    sentence = []

    i = 0
    while i != steps:
        sentence.append(word)
        next_word = stochastic_sample(markov, word)
        if next_word == '<STOP>':
            break
        word = next_word
        i += 1
        
    return sentence
    
if __name__ == "__main__":
    # file = 'static/corpus/sample_text.txt'
    file = 'static/corpus/islandofdrmoreau.txt'
    text = load_text(file)
    # print(text)
    clean = cleanup_text(text)
    endstop = add_stop(clean)
    pairs = find_pairs(endstop)
    # print(pairs)
    markov = markov_histo(pairs)
    # print(markov)
    # sample = stochastic_sample(markov, "i")
    # print(sample)

    init_word = choice([word for word in endstop if word != endstop[:-1]])
    # word = random_word(markov, init_word)
    word = stochastic_sample(markov, init_word)
    random_int = randint(3,10)
    walk = random_walk(init_word, markov, random_int)

    cap = " ".join(walk).capitalize()
    print(f"{cap}.")



