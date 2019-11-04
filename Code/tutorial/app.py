from flask import Flask, render_template
from random import randint
from stochastic import no_choice_freq_sample
from histogram import load_text, histogram

app = Flask(__name__)


@app.route('/')
def sentence_generator():
    text = "islandofdrmoreau.txt"
    source_text = load_text(text)
    histo = histogram(source_text)

    sentence = []
    sentence_length = randint(5, 15)

    while len(sentence) != int(sentence_length):
        random_word = no_choice_freq_sample(histo)
        sentence.append(random_word)

    cap = " ".join(sentence).capitalize()
    sentence = f"{cap}."
    return render_template('index.html', sentence=sentence)