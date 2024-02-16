#!/usr/bin/python3
"""0-hello_route: starts flask web application"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    "hello: displays 'Hello HBNB' on /"
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def HBNB_page():
    "HBNB_page: displays HBNB on /hbnb"
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    "c_text: Displays C followed by text value"
    text = text.replace("_", " ")
    return (f"C {escape(text)}")


if __name__ == "__main__":
    app.run(debug=True)
