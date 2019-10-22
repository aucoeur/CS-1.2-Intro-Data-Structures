from random import choice
import sys

def rearrange(words):
    unshuffled = words
    scrambled = []

    while len(scrambled) != len(unshuffled):
        random_word = choice(unshuffled)
        if random_word not in scrambled:
            scrambled.append(random_word)
               
    return ' '.join(scrambled)

def string_reverse(word):
    joined_word = ''.join(word)
    sliced_word = joined_word[::-1]
    return sliced_word

def sentence_reverse(sentence):
    reversed_sentence = string_reverse(sentence)
    return ' '.join(reversed_sentence)

if __name__ == "__main__":
    words = sys.argv[1:]
    # print(rearrange(words))
    # print(string_reverse(words))
    print(sentence_reverse(words))