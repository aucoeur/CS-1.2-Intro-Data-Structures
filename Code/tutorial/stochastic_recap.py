import sys
from random import randint, choices, randrange
from histogram import load_text, histogram

def recap_samp_freq(histo):

    '''
    use the pie chart/number line way
    sum up in steps
    dart = randint or randrange
    '''

    total = 0
    dart = randint(0, sum(histo.values()))
    print(histo.items())
    for each in histo.items():
        print(f"Total: {total} + {each[1]}")
        total += each[1]
        if dart <= total:
            return f"Dart: {dart} | Word: {each[0]}"

if __name__ == "__main__":
    text = 'sample_text2.txt'
    # text = 'islandofdrmoreau.txt'
    # text = sys.argv[1:]
    source_text = load_text(text)
    histo = histogram(source_text)
    recap = recap_samp_freq(histo)
    print(recap)
        
    # text = "one fish two fish red fish blue fish"

    # word_count = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

    #works but impractical
    # word_list=['blue', 'fish', 'fish', 'fish', 'fish', 'one', 'red', 'two']

    # index = randrange(len(word_list)) 

    # print(sum(histo.values()))

    # print(f"Dart: {dart}")