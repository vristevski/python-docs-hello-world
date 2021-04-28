from flask import Flask
import urllib3

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World from VR!"
