#!/usr/bin/python3
""" start a flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
	/: Displays 'Hello HBNB!'.
	/hnh: Displays 'HBNB'.
	/c/<text>: Displays 'C' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)
# condition strict_slashes=False
app.url_map.strict_slashes = False


@app.route("/")
def hello():
	""" print this message
	"""
	return "Hello HBNH!"


@app.route("/hbnb")
def hbnb():
	""" Display 'HBNB' """
	return "HBNB"


@app.route("/c/<text>")
def c(text):
	""" displays 'c' then the value of <text>. 
	"""
	text = text.replace("_", " ")
	return "C {}".format(text)


if __name__ == "__main__":
	app.run(host="0.0.0.0")
