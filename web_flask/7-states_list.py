#!/usr/bin/python3
"""
A script to handle eight routes in a Flask web app
Route 1: 0.0.0.0:5000/
Route 2: 0.0.0.0:5000/hbnb
Route 3: 0.0.0.0:5000/c/<text>
Route 4: 0.0.0.0:5000/python/<text>
Route 5: 0.0.0.0:5000/number/<n> => works only if "n" is a positive integer
Route 6: 0.0.0.0:5000/number_template/<n> =>
         works only if "n" is a positive integer
Route 7: 0.0.0.0:5000/number_odd_or_even/<n> =>
         works only if "n" is a positive integer
Route 8: 0.0.0.0:5000/states_list
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
states_dict = storage.all(State)
states_list = []
if states_dict:
    for state in states_dict.values():
        states_list.append(state)
else:
    pass


@app.teardown_appcontext
def teardown(exception):
    """
    A function to ensure the proper closing of the database connection after
    each serve
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    """
    A function to render templates/7-states_list.html when visiting the
    route /states_list
    """
    return render_template('7-states_list.html', states_list=states_list)

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
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_route(text="is cool"):
    """
    A function to display custom content when visiting the route /python/<text>
    """
    if "_" in text:
        text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """
    Displaying custom content when visiting the route /number/<int:n>
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    """
    Rendering custom template when visiting the route /number_template/<int:n>
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_route(n):
    """
    Rendering custom template when visiting the route
    /number_odd_or_even/<int:n>
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
