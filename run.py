#! /usr/bin/env python
from flask import Flask, render_template
import json
from random import choice

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True




@app.route("/")
def home():
    return render_template("index.html")




@app.route("/wir")
def cats():
    return render_template("wir.html")

@app.route("/spiel")
def spiel():
    return render_template("spiel.html")

@app.route("/manon")
def cat1():
    return render_template("manon.html")

@app.route("/ida")
def cat2():
    return render_template("ida.html")

@app.route("/mias")
def cat3():
    return render_template("mias.html")

@app.route("/alessandra")
def cat3():
    return render_template("alessandra.html")

if __name__ == "__main__":
    app.run()

