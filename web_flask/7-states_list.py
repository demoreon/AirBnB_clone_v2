#!/usr/bin/python3
"""
This script processes a Flask web APP.
The APP listens on 0.0.0.0, port 5000.
Routes:
/states_list: HTML page with a list of all State objects in DBStorage.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(exc):
    """close the current session of sqlalchemist"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all(State).values
    dict_to_html = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html',
                           Table="States",
                           items=dict_to_html)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
