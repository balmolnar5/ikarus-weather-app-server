import requests
from flask import jsonify


class WeatherService:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.current_weather_url = f"{base_url}/current.json"

    def get_current_weather(self, location: str) -> requests.Response:
        params = {"key": self.api_key, "q": location}

        try:
            response = requests.get(self.current_weather_url, params=params, timeout=10)
            response.raise_for_status()

            return response

        except Exception as e:
            if "not found" in str(e).lower():
                return jsonify({"error": "Location {location!r} not found"}), 404

            return jsonify({"error": "Weather service unavailable"}), 500
