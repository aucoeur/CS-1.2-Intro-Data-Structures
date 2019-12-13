from flask import Flask, render_template
from random import randint, choice
from format_text import load_text, cleanup_text, add_stop, structure_sentence
from narkov_chain import narkov_histo, random_walk, random_state
# from markov_chain import narkov_histo

app = Flask(__name__)

# text = "static/corpus/30rock.txt"
# text = "static/corpus/islandofdrmoreau.txt"
# text = "static/corpus/sample_text.txt"
text = "static/corpus/rpdr_full.txt"
# text = "static/corpus/simpsons.txt"

source_text = load_text(text)
cleaned = cleanup_text(source_text)
formatted_corpus = add_stop(cleaned)

markov = narkov_histo(formatted_corpus)

@app.route('/')
def index():

    random_int = randint(3,12)
    output = random_walk(markov, random_int)

    sentence = structure_sentence(output)

    return render_template('index.html', sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))