#!/usr/bin/python3
""" Web-application from Flask and Jinja """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def State_id_html():
    """Serves Jinja template files with State formatted inside"""

    container = storage.all('State').values()
    return (render_template('7-states_list.html', container=container))


@app.teardown_appcontext
def storage_close_call(exc=None):
    """Refreshes sessions after every request"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
