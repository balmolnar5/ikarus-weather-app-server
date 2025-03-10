import requests
from flask import current_app, jsonify


def get_current_weather(location):
    print(location)

    url = "http://api.weatherapi.com/v1/current.json"
    api_key = current_app.config.get("WEATHER_API_KEY")

    print(api_key)
    params = {"key": api_key, "q": location}

    # TODO: do this in the service
    response = requests.get(url, params=params, timeout=5)

    return jsonify(response.json()), 200
