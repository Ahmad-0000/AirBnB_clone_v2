#!/usr/bin/python3
"""
A script to handle two routes in a Flask web app
Route 1: 0.0.0.0:5000/states
Route 2: 0.0.0.0:5000/states/<id> => id must be a "uuid" string.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
states_dict = storage.all(State)
states_list = []
if states_dict:
    for state in states_dict.values():
        states_list.append(state)

@app.teardown_appcontext
def teardown(exception):
    """
    A function to ensure the proper closing of the database connection after
    each serve
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """
    A function to render the template 'templates/9-states.html'
    in a custom way when visiting the route '/states'
    """
    return render_template('9-states.html', states_list=states_list, var=False)

@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    A function to render the template 'templates/9-states.html' in
    another custom way when visiting the route '/states/<id>'
    """
    state = None
    for item in states_list:
        if id == item.id:
            state = item
            break
    return render_template('9-states.html', state=state, var=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
