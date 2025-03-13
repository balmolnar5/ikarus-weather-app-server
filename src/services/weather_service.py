import requests


class WeatherService:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.current_weather_url = f"{base_url}/current.json"

    def get_current_weather(self, location: str):
        params = {"key": self.api_key, "q": location}

        try:
            response = requests.get(self.current_weather_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            return self._transform_current_weather(data)

        except requests.exceptions.RequestException as err:
            raise Exception(f"Weather service unavailable: {str(err)}") from err

    def _transform_current_weather(self, api_data):
        # TODO: transform API response to the data model

        location = {
            "name": api_data["location"]["name"],
            "region": api_data["location"]["region"],
            "country": api_data["location"]["country"],
            "lat": api_data["location"]["lat"],
            "lon": api_data["location"]["lon"],
            "time_zone_id": api_data["location"]["tz_id"],
            "local_time_epoch_s": api_data["location"]["localtime_epoch"],
        }

        condition = {
            "code": api_data["current"]["condition"]["code"],
            "icon": api_data["current"]["condition"]["icon"],
            "text": api_data["current"]["condition"]["text"],
        }

        current_weather = {
            "condition": condition,
            "temp_c": api_data["current"]["temp_c"],
            "temp_f": api_data["current"]["temp_f"],
            "feelslike_c": api_data["current"]["feelslike_c"],
            "feelslike_f": api_data["current"]["feelslike_f"],
            "wind_speed_kph": api_data["current"]["wind_kph"],
            "wind_speed_mph": api_data["current"]["wind_mph"],
            "wind_direction_degree": api_data["current"]["wind_degree"],
            "wind_direction": api_data["current"]["wind_dir"],
            "humidity": api_data["current"]["humidity"],
            "is_day": bool(api_data["current"]["is_day"]),
            "last_updated_epoch_s": api_data["current"]["last_updated_epoch"],
            "uv": api_data["current"]["uv"],
        }

        weather_response = {
            "location": location,
            "current_weather": current_weather,
        }

        return weather_response
