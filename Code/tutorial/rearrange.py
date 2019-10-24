from random import choice
import sys

def rearrange(words):
    unshuffled = words.copy()
    scrambled = []

    # while len(scrambled) != len(unshuffled):
    #     random_word = choice(unshuffled)
    #     if random_word not in scrambled:
    #         scrambled.append(random_word)
    while len(unshuffled) > 0:
        random_word = choice(unshuffled)
        scrambled.append(random_word)
        unshuffled.remove(random_word)
                       
    return ' '.join(scrambled)

def string_reverse(word):
    joined_word = ''.join(word)
    sliced_word = joined_word[::-1]
    return sliced_word

def sentence_reverse(sentence):
    reversed_sentence = sentence[::-1]
    return ' '.join(reversed_sentence)

def fisher_yates(words):
    for word in words:
        random_word = choice(words)

        x = words.index(word)
        y = words.index(random_word)

        words[x], words[y] = words[y], words[x]
    
    return ' '.join(words)

if __name__ == "__main__":
    words = sys.argv[1:]
    # print(rearrange(words))
    # print(string_reverse(words))
    # print(sentence_reverse(words))
    print(fisher_yates(words))