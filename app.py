from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

@app.route('/fortune')
def fortune():
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    animal = request.args.get('animal')
    horoscope = request.args.get('horoscope')



    if animal == 'bunny':
        return render_template('bunny.html')
    elif animal == 'doggo':
        return render_template('doggo.html')
    elif animal == 'cat':
        return render_template('cat.html')
    elif animal == 'birb':
        return render_template('birb.html')
    elif animal == 'horse':
        return render_template('horse.html')



    if __name__ == '__main__':
        app.run()
