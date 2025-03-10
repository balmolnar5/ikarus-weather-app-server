import os
from connexion import FlaskApp
from dotenv import load_dotenv
from pathlib import Path


app = FlaskApp(__name__)

load_dotenv()


def main() -> None:
    app.add_api(specification="../openapi.yaml")
    # app.run(f"{Path(__file__).stem}:app")
    app.app.config["WEATHER_API_KEY"] = os.getenv("WEATHER_API_KEY")

    app.run()


if __name__ == "__main__":
    main()
