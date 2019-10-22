from random import choice
import sys

def rearrange():
    unshuffled = sys.argv[1:]
    scrambled = []

    while len(scrambled) != len(unshuffled):
        random_word = choice(unshuffled)
        if random_word not in scrambled:
            scrambled.append(random_word)
               
    print(' '.join(scrambled))

if __name__ == "__main__":
    rearrange()