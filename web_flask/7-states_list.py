#!/usr/bin/python3
'''
A script to render a specific page when visiting the route "/states_list"
'''
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
    return render_template('7-states_list.html', states_list=states_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
