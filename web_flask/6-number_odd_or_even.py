#!/usr/bin/python3
"""starts flask web application"""

from flask import Flask, render_template
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


# shows implementation of different data type input
@app.route("/number/<int:n>", strict_slashes=False)
def n_number(n):
    "n_number: returns string only if n is a number"
    return (f"{n} is a number")


# shows implementation of template construction
@app.route("/number_template/<int:n>", strict_slashes=False)
def html_number(n):
    "n_number: returns html only if n is a number"
    return render_template('5-number.html', n=n)


# shows implementations of expressions
@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """odd_or_even: returns the state of a number in a html page"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(debug=True)
