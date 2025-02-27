#!/usr/bin/python3

"""Launches a simple Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
   /hbnb: Displays "HBNB!'
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
