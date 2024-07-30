#!/usr/bin/python3
"""
Flask application that lists all states from DBStorage
"""

import os
import sys
from flask import Flask, render_template


def setup_path_and_imports():
    """Adjusts sys.path and imports necessary modules"""
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append(parent_dir)
    global storage, State
    from models import storage
    from models.state import State


setup_path_and_imports()


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of all State objects"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
