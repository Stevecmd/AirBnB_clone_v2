#!/usr/bin/python3
"""
Flask application that lists all states and cities from DBStorage
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exc):
    """Closes the storage on teardown."""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page with a list of all State objects
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays a HTML page with a list of City objects linked to the State."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
