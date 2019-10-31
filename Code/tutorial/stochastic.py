import sys
from random import randint, choices, randrange
from histogram import load_text, histogram

def sampler(histo):
    histo_keys = [key for key in histo]
    rand_num = randint(0, len(histo_keys)-1)

    return histo_keys[rand_num]

def sample_by_freq(histo):
    histo_keys = [key for key in histo]
    total_tokens = sum(histo.values())

    weighted_values = []
    for value in histo.values():
        weighted = value / total_tokens
        weighted_values.append(weighted)

    weighted_choice = choices(histo_keys, weighted_values, k=1)
    
    chosen_word = "".join(weighted_choice)
    word_index = histo_keys.index(chosen_word)

    return f"{chosen_word}: {weighted_values[word_index]}"

def no_choice_freq_sample(histo):

    '''
    use the pie chart/number line way
    sum up in steps
    dart = randint or randrange
    '''

    total = 0
    dart = randint(0, sum(histo.values()))

    for each in histo.items():
        # print(f"Total: {total} + {each[1]}")
        total += each[1]
        if dart <= total:
            # return f"Dart: {dart} | Word: {each[0]}"
            return each[0]

if __name__ == "__main__":
    text = 'sample_text2.txt'
    # text = 'islandofdrmoreau.txt'
    # text = sys.argv[1:]
    source_text = load_text(text)
    histo = histogram(source_text)
    # print(weighted_sampler(histo))
    # weighted_sampler(histo)
    tracker = {}
    count = 0
    while count != 1000:
        # word = sample_by_freq(histo)
        word = no_choice_freq_sample(histo)     
        # No .append() for dict. To add new key to dict, use assignment operator with dict key.
        tracker[word] = tracker.get(word, 0) + 1
        count += 1
    print(tracker)
        
