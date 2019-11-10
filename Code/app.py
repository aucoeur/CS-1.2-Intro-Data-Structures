from flask import Flask, render_template
from random import randint, choice
from stochastic import no_choice_freq_sample
from histogram import load_text, histogram
from markov_chain import random_walk, random_word, make_markov

app = Flask(__name__)


@app.route('/')
def sentence_generator():
    text = "static/corpus/30rock.txt"
    # text = "static/corpus/islandofdrmoreau.txt"
    # text = "static/corpus/sample_text.txt"
    # text = "static/corpus/rpdr.txt"
    source_text = load_text(text)

    # histo = histogram(source_text)

    # sentence = []
    # sentence_length = randint(5, 15)

    # while len(sentence) != int(sentence_length):
    #     random_word = no_choice_freq_sample(histo)
    #     sentence.append(random_word)

    markov = make_markov(source_text)

    #TODO: investigate why still returns last word occasionally? (temp janky fix with random_word randint total_links-2)
    init_word = choice([word for word in source_text if word != source_text[-1]])

    word = random_word(markov, init_word)

    random_int = randint(3,10)
    sentence = random_walk(word, markov, random_int)

    cap = " ".join(sentence).capitalize()
    sentence = f"{cap}."

    return render_template('index.html', sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))