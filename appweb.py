#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)
def failasomma(a: int, b: int):
    return a+b


@app.route('/')
def hello_world():
    a = 1
    b = 2
    somma = failasomma(a, b)

    return f'<span style="color: red;">{somma}</span>'

@app.route('/hello/<x>')
def hello_x(x):
    return f'<span style="color: red;">Hello {x}</span>'
