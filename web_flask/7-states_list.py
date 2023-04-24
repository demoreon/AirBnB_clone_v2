#!/usr/bin/python3
"""
A simple Flask web application that lists
"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """ close the current session of sqlalchemist """
    storage.close()


@app.route('/states_list')
def states_list():
    """ States are sorted by name. """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
