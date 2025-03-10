from connexion import FlaskApp

app = FlaskApp(__name__)


def post_greeting(name: str):
    return f"Hello {name}", 200


def main() -> None:
    app.add_api("openapi.yaml")
    app.run()


if __name__ == "__main__":
    main()
