from flask import Flask, render_template
from random import randint, choice
from stochastic import no_choice_freq_sample
from format_text import load_text, cleanup_text, add_stop, structure_sentence
from markov_chain import find_pairs, markov_histo, stochastic_sample, random_walk

app = Flask(__name__)


@app.route('/')
def sentence_generator():
    # text = "static/corpus/30rock.txt"
    # text = "static/corpus/islandofdrmoreau.txt"
    # text = "static/corpus/sample_text.txt"
    # text = "static/corpus/rpdr.txt"
    text = "static/corpus/simpsons.txt"

    source_text = load_text(text)
    cleaned = cleanup_text(source_text)
    formatted_corpus = add_stop(cleaned)

    pairs = find_pairs(formatted_corpus)
    markov = markov_histo(pairs)

    init_word = choice([word for word in formatted_corpus if word != formatted_corpus[:-1]])

    word = stochastic_sample(markov, init_word)
    random_int = randint(3,12)
    output = random_walk(word, markov, random_int)

    sentence = structure_sentence(output)

    return render_template('index.html', sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))