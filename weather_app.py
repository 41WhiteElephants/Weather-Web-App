"""Application's main script. It provides site routing, http
requests service as well as automatic opening of default browser's
window. Script is using OpenWeatherMaps API. It is necessary to
use python3 due to displaying UTF signs properly.

usage:
    python3 weather_app.py
"""
import webbrowser

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
import requests
from wtforms import DecimalField
from wtforms.validators import InputRequired, ValidationError


app = Flask(__name__)
app.config['SECRET_KEY'] = 'teachairrisk'


def check_latitude(form, field):
    if not -80 < field.data < 80:
        raise ValidationError('Latitude must be a number between -80 and 80')


def check_longitude(form, field):
    if not -180 < field.data < 180:
        raise ValidationError('Longitude must be a number between -180 and 180')


class CoordinatesForm(FlaskForm):
    latitude_bottom = DecimalField('latitude_bottom', validators=[InputRequired(), check_latitude])
    longitude_left = DecimalField('longitude_left', validators=[InputRequired(), check_longitude])
    latitude_top = DecimalField('latitude_top', validators=[InputRequired(), check_latitude])
    longitude_right = DecimalField('longitude_right', validators=[InputRequired(), check_longitude])


def get_mean_temp(station_temp_dicterature):
    """Get mean temperature.
    Args:
        station_temp_dicterature(dict): dict of pairs (station name : temperature)
    Returns:
        mean_temp(str): mean temperature of all stations results
    """
    temp_sum = sum(temp for temp in station_temp_dicterature.values())
    mean_temp = temp_sum / len(station_temp_dicterature)
    return '%.1f' % mean_temp


def get_stations_temperatures(lon_left, lat_bottom, lon_right, lat_top):
    """Function gets all stations in the area & their temperatures drawn by a rectangle,
    which has opposite vertices in the points (lon_left, lat_bottom)
    & (lon_right, lat_top). Uses openWeatherMaps API.
    Args:
        lon_left(float): longitude of the left bottom vertex
        lat_bottom(float): latitude of the left bottom vertex
        lon_right(float): longitude of the right top vertex
        lat_top(float): latitude of the right top vertex
    Returns:
        station_temp_dicterature(dict) : dictionary with pairs (station_name : temperature)
    """
    response = requests.get('http://api.openweathermap.org/data/2.5/box/city?bbox={},{},{},{},10'
                            '&appid=0a31749b47bc89f410b57d12a7cdee7b'.format(lon_left, lat_bottom, lon_right, lat_top))
    json_response = response.json()
    station_temp_dicterature = {item['name']: item['main']['temp'] for item in json_response['list']}
    return station_temp_dicterature


@app.route('/index', methods=['POST', 'GET'])
def index():
    """Function is mapping URL of the website with this function.
    Using open weather maps API gets temperature in Kelvin degrees
    & converts it to Celsius degrees. Then, renders it.
    """
    form = CoordinatesForm()
    if form.validate_on_submit():
        station_temp_dicterature = get_stations_temperatures(form.longitude_left.data, form.latitude_bottom.data,
                                                             form.longitude_right.data, form.latitude_top.data)
        mean_temp = get_mean_temp(station_temp_dicterature)
        return render_template('result.html', mean_temp=mean_temp,
                               station_temp_dicterature=station_temp_dicterature)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    url = 'http://localhost:5000/index'
    webbrowser.open_new_tab(url)
    app.run(debug=True)


