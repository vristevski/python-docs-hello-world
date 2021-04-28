from flask import Flask
import urllib.request

app = Flask(__name__)

@app.route("/")
def hello():
    with urllib.request.urlopen('http://www.brainjar.com/java/host/test.html') as response:
    html = response.read()
    #print(html)
    return html
    #return "Hello, World from VR!"
