[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# ikarus-weather-app-server

The back-end (Flask) of a simple weather app that fetches real-time weather data.

## Project Setup

Versions used for development:

-   python: 3.13.2
-   pip: 25.0.1

Steps:

1. Use Python 3
1. Setup a virtual environment (e.g., with `venv`) and install the package dependencies (`pip install -r requirements.txt`)
1. Create a `.env` file and paste the API key received into it (see `.env.example`)
1. Start the dev server by running `src/run.py`:
    - `cd src/`
    - `python run.py`
    - (or `uvicorn run:app`)
