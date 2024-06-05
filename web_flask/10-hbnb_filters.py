#!/usr/bin/python3
"""
A Flask wep app that handles one route
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
states_dict = storage.all(State)
states_list = []
if states_dict:
    for state in states_dict.values():
        states_list.append(state)


cities_dict = storage.all(City)
cities_list = []
if cities_dict:
    for city in cities_dict.values():
        cities_list.append(city)

amenities_dict = storage.all(Amenity)
amenities_list = []
if amenities_dict:
    for amenity in amenities_dict.values():
        amenities_list.append(amenity)

@app.teardown_appcontext
def teardown(exception):
    """
    A function to ensure the proper closing of the database connection after
    each serve
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    A function to render the template "templates/10-hbnb_filters.html"
    when visiting the route "/hbnb_filters"
    """
    return render_template('10-hbnb_filters.html', states_list=states_list,
                           cities_list=cities_list,
                           amenities_list=amenities_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
