from flask import Flask
import urllib.request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World from VR!"
