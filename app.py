#idk
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def hello_world():
    return "Hello World!"

app.run(debug=True, port=8080)