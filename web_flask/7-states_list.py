#!/usr/bin/python3
'''
A script to render a specific page when visiting the route "/states_list"
'''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
all_states = storage.all(State)


@app.teardown_appcontext
def teardown(exception):
    '''
    A function to ensure the proper closing of the database connection after
    each serve
    '''
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    '''
    A function to render "templates/7-states_list.html" when visiting the
    route "/states_list"
    '''
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
