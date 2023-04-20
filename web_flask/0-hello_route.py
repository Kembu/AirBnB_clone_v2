#!/usr/bin/python3
"""Flask script which displays route/ “Hello HBNB!” """
from flask import Flask

app = Flask(__name__)
@app.route("/", strict_slashes=False)
def index():
    """Function to define index"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 
