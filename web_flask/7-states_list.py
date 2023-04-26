#!/usr/bin/python3
"""Starts a Flask web application.

Routes:
    /states_list: Displays a list of all State objects in the database.

"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of all State objects in the database."""
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removes the current SQLAlchemy Session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
