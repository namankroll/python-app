from flask import Flask
from random import random2
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"
