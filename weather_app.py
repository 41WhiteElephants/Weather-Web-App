"""Application's main script. It provides site routing, http
requests service as well as automatic opening of default browser's
window. Script is using OpenWeatherMaps API. It is necessary to
use python3 due to displaying UTF signs properly.

usage:
	python3 weather_app.py
"""
import webbrowser

from flask import Flask, request, render_template
import requests


app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
def index():
    """Function is mapping URL of the website with this function.
    Using open weather maps API gets temperature in Kelvin degrees
    & converts it to Celsius degrees. Then, renders it.
    """
    if request.method == 'POST':
        coordinates = request.form['data']
        if coordinates == '' or not coordinates.isdigit():
            return render_template('error.html')
        try:
            latitude, longitude = coordinates.split()
            if -80 < float(latitude) < 80 or -180 < float(longitude) < 180:
                return render_template('error.html')
        except ValueError:
            return render_template('error.html')
        finally:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}'
                                   '&appid=0a31749b47bc89f410b57d12a7cdee7b'.format(latitude, longitude))
            json_response = response.json()
            station_name = str(json_response['name'])
            kelvin_degrees = float(json_response['main']['temp'])
            temperature = kelvin_degrees - 272.15
            return render_template('result.html', name=station_name, temperature="{:.1f}".format(temperature))
    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    url = 'http://localhost:5000/index'
    webbrowser.open(url, 1)
    app.run(debug=True)


