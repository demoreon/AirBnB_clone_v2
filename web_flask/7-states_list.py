#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()

    @app.route('/states_list', strict_slashes=False)
def display_html():
    """ A swift function call"""
    data = storage.all(State)
    return render_template('templates/7-states_list.html', total=data.values())
    if _fg_name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
