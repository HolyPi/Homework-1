from flask import Flask, render_template, request
import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

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

@app.route('/weather')
def weather():
    return render_template('weather_form.html')

@app.route('/weather_results')
def weather_results_page():
    users_city = request.args.get('city')

    params = {
    'q': users_city,
    'appid': '2608f679d4594364525f6c6cc2246c79'

    }
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)
    if not response.status_code == 200:

        print("Nothing to show")

    results = response.json()

    city = results['name']

    temp = convert(results['main']['temp'])

    return render_template('weather_results.html', city=city, temp=temp)

def convert(K):
    conversion = 9/5 * (K - 273) + 32
    return int(conversion)

    if __name__ == '__main__':
        app.run()
