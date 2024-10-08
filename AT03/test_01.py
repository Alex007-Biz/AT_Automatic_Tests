import pytest
from main_01 import get_weather

api_key = '837f0aa0103469641de4270ffb811a57'
city = 'London'

def test_get_weather(mocker):
    mock_get = mocker.patch('main_01.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather' : [{'description': 'clear sky'}],
        'main' : {'temp': 273.15}
    }

    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather' : [{'description': 'clear sky'}],
        'main' : {'temp': 273.15}
    }

def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('main_01.requests.get')
    mock_get.return_value.status_code = 404
    weather_data = get_weather(api_key, city)

    assert weather_data == None