#!/usr/bin/python3
"""
A script to start a Flask web app with one route.
Route: 0.0.0.0:5000/
"""
from flask import Flask


app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    """A function to display content when visiting the root URL"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
