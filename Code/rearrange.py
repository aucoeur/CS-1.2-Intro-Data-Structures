from random import randint
import sys

def rearrange():

    unshuffled = sys.argv[1:]
    scrambled = []

    count = 0
    while count < len(unshuffled):
        rand_num = randint(1, len(unshuffled))
        rand_word = sys.argv[rand_num]
        if rand_word in scrambled:
            rand_word = sys.argv[rand_num]
        else:
            scrambled.append(rand_word)
            count += 1
    
    print(' '.join(scrambled))

if __name__ == "__main__":
    rearrange()