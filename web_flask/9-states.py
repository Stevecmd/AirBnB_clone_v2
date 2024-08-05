#!/usr/bin/python3
""" Flask application that lists all states and cities from DBStorage """
from flask import Flask, render_template, jsonify
from models import storage
from models.state import State
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.teardown_appcontext
def teardown_db(exc):
    """Closes the storage on teardown."""
    logging.debug("Tearing down the database connection")
    storage.close()
    logging.debug("Database connection closed")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template(
        "9-states.html",
        states=None,
        state=None,
        cities=None
    ), 500


@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page with a list of all State objects"""
    try:
        logging.debug("Fetching all states from storage")
        states_dict = storage.all(State)
        logging.debug(f"Fetched states: {states_dict}")
        return render_template("9-states.html", states=states_dict, state=None)
    except Exception as e:
        logging.error(f"Error fetching states: {e}", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays a HTML page with a list of City objects linked to the State."""
    try:
        logging.debug(f"Fetching state with id {id} from storage")
        state = storage.all(State).get(id)
        logging.debug(f"Fetched state: {state}")
        if state:
            logging.debug(f"State found: {state}")
            cities = state.cities
            logging.debug(f"Cities linked to state: {cities}")
            return render_template(
                "9-states.html",
                states=storage.all(State),
                state=state,
                cities=cities
            )
        else:
            logging.warning(f"No state found with id {id}")
            return render_template("404.html"), 404
    except Exception as e:
        logging.error(f"Error fetching state with id {id}: {e}", exc_info=True)
        return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0")
