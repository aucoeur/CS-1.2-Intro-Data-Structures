from queue import Queue
from random import randint, randrange, choice
from format_text import load_text, cleanup_text, add_stop
from dictogram import Dictogram

from utils import time_it

# @time_it
def markov_histo(corpus):
    '''Creates markov chain with histogram'''
    markov_dict = {}

    # First Order Markov
    for i in range(len(corpus)-1):
        first = corpus[i]
        second = corpus[i+1]

        if first not in markov_dict.keys():
            markov_dict[first] = Dictogram()
        
        markov_dict.get(first).add_count(second)
    
    return markov_dict

def narkov_histo(corpus):
    '''Creates an n-th order markov chain with histogram'''

    markov_dict = {}
    
    # 2nd Order Markov
    for i in range(len(corpus)-1):
        first = corpus[i]
        second = corpus[i+1]
        
        if second != '<STOP>':
            third = corpus[i+2]
            
            key = (first, second)    
            if key not in markov_dict.keys():
                markov_dict[key] = Dictogram()
            
            markov_dict.get(key).add_count(third)
        
    return markov_dict

def random_state(markov):
    '''Gets states with word as first in tuple'''
    states = [state for state in markov.keys()]
    return choice(states)

# @time_it
def stochastic_sample(markov, item):
    '''Gets a weighted random word from given word's histo'''
    histo = markov.get(item, 'NOPE')
    
    if item in markov:
        return histo.sample()
 
# @time_it
def random_walk(markov, steps):
    '''Given a starting word, picks a random word from markov list and walks to given number of steps to generate a sentence'''
    
    sentence = []
    q = Queue()
    
    states = random_state(markov)
    q.enqueue(states[0])
    q.enqueue(states[1])
    # print(f'Queue: {q}')

    i = 2
    while i != steps:
        # print(f"States: {states}")
        # rand_state = choice(states)
        # print(f"Random State: {rand_state}")
        
        # next_word = rand_state[1]
        next_word = stochastic_sample(markov, states)
        # print(f"Sample: {next_word}")

        if len(q) == 3:
            entry = q.dequeue()
            sentence.append(entry)
        q.enqueue(next_word)
        # print(f'Queue: {q}')
        
        next_state = (states[1], next_word)
        next_word = stochastic_sample(markov, next_state)
        # print(f"Sample: {next_word}")

        if len(q) == 3:
            entry = q.dequeue()
            sentence.append(entry)
        q.enqueue(next_word)
        # print(f'Queue: {q}\n')

        if next_word == '<STOP>':
            break
        
        states = (next_state[1], next_word)
        # print(f'{states}')

        i += 1
        
    return sentence
    
if __name__ == "__main__":
    # file = 'static/corpus/sample_text2.txt'
    file = 'static/corpus/rpdr.txt'
    # file = 'static/corpus/importbeingearnest.txt'
    text = load_text(file)
    # print(text)
    clean = cleanup_text(text)
    endstop = add_stop(clean)
    # pairs = find_pairs(endstop)
    # pairs = get_states(endstop)
    # print(pairs)

    # markov = markov_histo(endstop)
    markov = narkov_histo(endstop)
    # print(f"Markov Dicto: {markov} \n")

    # init_word = 'i'
    # states = get_states(init_word, markov)
    # print(f"States: {states}")
    # rand_state = choice(states)
    # print(f"Random State: {rand_state}")

    # sample = stochastic_sample(markov, rand_state)
    # print(f"Sample: {sample}")

    # # next_word = rand_state[1]
    # next_word = sample
    # q = Queue()
    # if len(q) == 2:
    #     q.dequeue()
    # enq = q.enqueue(next_word)
    # print(f'Queue: {q}')


    # init_word = choice([word for word in endstop if word != endstop[:-1]])
    # init_word = ('i', 'like')
    # init_word = rand_state[1]
    # word = stochastic_sample(markov, init_word)
    # random_int = randint(3,9)
    # walk = random_walk(init_word, markov, random_int)
    for i in range(15):
        walk = random_walk(markov, 10)
        # print(walk)

        cap = " ".join(walk).capitalize()
        print(f"{cap}.")