#!/usr/bin/python3
"""starts flask web application"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


# shows basic Flask implementation
@app.route("/", strict_slashes=False)
def hello():
    "hello: displays 'Hello HBNB' on /"
    return ("Hello HBNB!")


# shows basic URL implementation
@app.route("/hbnb", strict_slashes=False)
def HBNB_page():
    "HBNB_page: displays HBNB on /hbnb"
    return ("HBNB")


# shows dynamic url implementation
@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    "c_text: Displays C followed by text value"
    text = text.replace("_", " ")
    return (f"C {escape(text)}")


# Shows implementation of optional URL paths
@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def p_text(text="is cool"):
    "p_text: Displays 'Python' followed by text value"
    text = text.replace("_", " ")
    return (f"Python {escape(text)}")


if __name__ == "__main__":
    app.run(debug=True)
