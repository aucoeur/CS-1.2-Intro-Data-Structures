from flask import Flask
from random import randint
from stochastic import no_choice_freq_sample
from histogram import load_text, histogram

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello Girl"

@app.route('/gen')
def sentence_generator():
    text = "islandofdrmoreau.txt"
    source_text = load_text(text)
    histo = histogram(source_text)

    sentence = []
    sentence_length = randint(5, 15)

    while len(sentence) != int(sentence_length):
        random_word = no_choice_freq_sample(histo)
        sentence.append(random_word)

    sentence = " ".join(sentence).capitalize()
    return f'{sentence}.'