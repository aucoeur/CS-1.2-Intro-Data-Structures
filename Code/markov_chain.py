from random import randint, randrange, choice
from format_text import load_text, cleanup_text, add_stop
from dictogram import Dictogram
from utils import time_it

# @time_it
def markov_histo(corpus):
    '''Creates markov chain with histogram'''
    markov_dict = {}

    for i in range(len(corpus)-1):
        first = corpus[i]
        second = corpus[i+1]

        if first not in markov_dict.keys():
            markov_dict[first] = Dictogram()
        
        markov_dict.get(first).add_count(second)
    
    return markov_dict

# @time_it
def stochastic_sample(markov, word):
    '''Gets a weighted random word from given word's histo'''
    histo = markov.get(word, 'NOPE')
    
    if word in markov:
        return histo.sample()
 
# @time_it
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
    file = 'static/corpus/sample_text.txt'
    # file = 'static/corpus/islandofdrmoreau.txt'
    text = load_text(file)
    # print(text)
    clean = cleanup_text(text)
    endstop = add_stop(clean)
    # pairs = find_pairs(endstop)
    # pairs = get_states(endstop)
    # print(pairs)

    markov = markov_histo(endstop)
    print(markov)
    # sample = stochastic_sample(markov, "i")
    # print(sample)

    init_word = choice([word for word in endstop if word != endstop[:-1]])
    # init_word = 'i'
    word = stochastic_sample(markov, init_word)
    random_int = randint(3,10)
    walk = random_walk(init_word, markov, random_int)

    cap = " ".join(walk).capitalize()
    print(f"{cap}.")



