import sys
from random import randint, choices
from histogram import load_text, histogram

def sampler(histo):
    histo_keys = [key for key in histo]
    rand_num = randint(0, len(histo_keys) -1)

    return histo_keys[rand_num]

def weighted_sampler(histo):
    histo_keys = [key for key in histo]
    values = [value for value in histo.values()]

    weighted_values = []
    for value in values:
        weighted = value / len(histo)
        weighted_values.append(weighted)

    weighted_choice = choices(range(len(values)), weighted_values)
    
    return histo_keys[weighted_choice[0]]

if __name__ == "__main__":
    text = 'sample_text2.txt'
    # text = 'islandofdrmoreau.txt'
    # text = sys.argv[1:]
    source_text = load_text(text)
    histo = histogram(source_text)
    print(weighted_sampler(histo))
    # weighted_sampler(histo)