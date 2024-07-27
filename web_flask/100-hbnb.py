#!/usr/bin/python3
"""
Flask application that displays filters for states, amenities, and places
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays a HTML page with filters for states, amenities, and places"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html',
                           states=sorted(states, key=lambda x: x.name),
                           amenities=sorted(amenities, key=lambda x: x.name),
                           places=sorted(places, key=lambda x: x.name))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
