from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    animal = request.args.get('animal')
    


    if animal == 'bunny':
        fortune is "Some bunny loves you!"
    elif animal == 'doggo':
        fortune is "Don't fur-get that you're the best!"
    elif animal == 'cat':
        fortune is "Cat-titude is everything!"
    elif animal == 'birb':
        fortune is "You're im-peck-able!"
    elif animal == 'horse':
        fortune is "Hay, you'll have a fantastic day!"




    return render_template('fortune_results.html', fortune=fortune)

    if __name__ == '__main__':
        app.run()
