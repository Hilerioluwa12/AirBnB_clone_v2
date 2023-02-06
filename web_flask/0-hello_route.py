#!/usr/bin/python3
""" Create a web application that listen in port 5000 flask
Routes:
	/: Displays 'Hello HBNB!'
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
	""" print this message
	"""
	return "Hello HBNB!"

if __name__ == "__main__":
	""" config the run
	"""
	app.run(host='0.0.0.0', port=5000)
