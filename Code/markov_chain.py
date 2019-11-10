from random import randint, randrange, choice
from histogram import load_text
import dictogram

def make_markov(corpus):
    '''Creates word pairs and puts them into a markov dictionary'''

    pairs = []

    for i in range(len(corpus)-1):
        pairs.append((corpus[i], corpus[i+1]))
    
    markov_dict = {}

    for first, second in pairs:
        if first in markov_dict.keys():
            markov_dict[first].append(second)
        else:
            markov_dict[first] = [second]
    return markov_dict

def random_word(markov, word):
    '''Takes given word and returns a random word in its markov list'''
    total_links = len(markov[word])
    if total_links >= 2:
        random = randint(0, total_links-1) #janky fix to avoid picking last word
        if total_links == 1:
            random = randint(0, 1)
        chain = markov[word][random]
    else:
        chain = markov[word][0]
    return chain

def random_walk(word, markov, steps):
    '''Given a starting word, picks a random word from markov list and walks to given number of steps to generate a sentence'''

    sentence = []

    sentence.append(word)

    i = 0
    while i != steps:
        next_word = random_word(markov, word)
        word = next_word
        sentence.append(word)
        i += 1
    
    return sentence
    
if __name__ == "__main__":
    file = '/static/corpus/sample_text.txt'
    # file = 'islandofdrmoreau.txt'
    text = load_text(file)
    # print(text)
    markov = make_markov(text)
    # print(markov['i'])
    # print(len(markov['i']))
    # print(text)
    # print(text[-1])
    # init_word = choice([word for word in text if word != text[-1]])
    # word = random_word(markov, init_word)
    # random_int = randint(3,9)
    # walk = random_walk(word, markov, random_int)

    # cap = " ".join(walk).capitalize()
    # print(f"{cap}.")



