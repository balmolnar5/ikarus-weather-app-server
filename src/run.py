import os
from pathlib import Path

from connexion import FlaskApp
from dotenv import load_dotenv

load_dotenv()

app = FlaskApp(__name__)

app.add_api(specification="../openapi.yaml")

app.app.config["WEATHER_API_KEY"] = os.getenv("WEATHER_API_KEY")
app.app.config["WEATHER_API_BASE_URL"] = "http://api.weatherapi.com/v1"


def main() -> None:
    app.run(f"{Path(__file__).stem}:app")


if __name__ == "__main__":
    main()
