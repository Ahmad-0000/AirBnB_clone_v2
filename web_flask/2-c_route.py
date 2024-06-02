#!/usr/bin/python3
"""
A script to handle three routes in a Flask web app
Route 1: 0.0.0.0:5000/
Route 2: 0.0.0.0:5000/hbnb
Route 3: 0.0.0.0:5000/c/<text>
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """A function to display content when visiting the root URL"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """A function to dispaly content when visiting the route /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    A function to display custom content when visiting the route /c/<text>
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
