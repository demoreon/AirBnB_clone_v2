#!/usr/bin/python3
"""A Simple flask web application that lists states"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_storage(exception=None):
    """Closes the current SQLAlchemy session"""
    storage.close()


@app.route('/states_list')
def state_list():
    """Returns a rendered HTML template"""
    from models.state import State
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
app.run(host="0.0.0.0", port=5000)
