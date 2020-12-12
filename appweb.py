#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    a = 1
    b = 2
    somma = a+b

    return f'<span style="color: red;">{somma}</span>'
