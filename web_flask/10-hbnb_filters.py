#!/usr/bin/python3
"""
Flask application that displays filters for states and amenities
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page with filters for states and amenities"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        '10-hbnb_filters.html',
        states=sorted(states, key=lambda x: x.name),
        amenities=sorted(amenities, key=lambda x: x.name)
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
