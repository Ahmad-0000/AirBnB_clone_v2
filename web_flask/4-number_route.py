#!/usr/bin/python3
"""
A script to handle five routes in a Flask web app
Route 1: 0.0.0.0:5000/
Route 2: 0.0.0.0:5000/hbnb
Route 3: 0.0.0.0:5000/c/<text>
Route 4: 0.0.0.0:5000/python/<text>
Route 5: 0.0.0.0:5000/number/<n> => works only if "n" is a positive integer
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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_route(text="is cool"):
    """
    A function to display custom content when visiting the route /python/<text>
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """
    Displaying custom content when visiting the route /number/<int:n>
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
