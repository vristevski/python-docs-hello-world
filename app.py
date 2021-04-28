from flask import Flask
import urllib.request

app = Flask(__name__)

@app.route("/")
def hello():
    with urllib.request.urlopen('http://ise-www.internal.cloudapp.net') as response:
        html = response.read()
    #print(html)
    return html
    #return "Hello, World from VR!"
