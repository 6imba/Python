from flask import Flask
from urllib import request
import os
from fontTools import ttLib

app = Flask(__name__)

# Members API Route:
@app.route("/")
def retriveFontData(url):
    return url+" apple"

if __name__ == "__main__":
    app.run(debug=True)

