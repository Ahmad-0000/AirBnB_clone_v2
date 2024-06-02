#!/usr/bin/python3
"""
A script to handle two routes in a Flask web app
Route 1: 0.0.0.0:5000/
Route 2: 0.0.0.0:5000/hbnb
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """A function to display content when visiting the root URL"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """A function to dispaly content when visisting the route /hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
