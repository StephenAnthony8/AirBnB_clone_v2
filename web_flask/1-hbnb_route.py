#!/usr/bin/python3
"""0-hello_route: starts flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    "hello: displays 'Hello HBNB' on /"
    return ("Hello HBNB!")


@app.route("/hbnb/", strict_slashes=False)
def HBNB_page():
    "HBNB_page: displays HBNB on /hbnb"
    return ("HBNB")


if __name__ == "__main__":
    app.run(debug=True)
