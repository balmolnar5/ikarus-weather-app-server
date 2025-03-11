from flask import current_app, jsonify

from services.weather_service import WeatherService


def get_current_weather(location: str):
    if not location or len(location.strip()) == 0:
        return jsonify({"error": "Location parameter is required"}), 400

    weather_service = WeatherService(
        api_key=current_app.config.get("WEATHER_API_KEY"),
        base_url=current_app.config.get("WEATHER_API_BASE_URL"),
    )

    data = weather_service.get_current_weather(location)

    return jsonify(data.json()), 200
