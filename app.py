import os

from flask import Flask

app = Flask(__name__)


def get_message(name: str = "World") -> str:
    return f"Hello, {name}!"


@app.route("/")
def home():
    name = os.getenv("APP_NAME", "World")
    return get_message(name), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8081"))
    app.run(host="0.0.0.0", port=port)
