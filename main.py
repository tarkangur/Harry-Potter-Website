import requests
from flask import Flask, render_template, url_for, request, redirect, flash


ENDPOINT = "https://api.potterdb.com/v1/"


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/books", methods=["GET"])
def books():
    return render_template('books.html')


@app.route("/films", methods=["GET"])
def films():
    return render_template('films.html')


@app.route("/spells", methods=["GET"])
def spells():
    return render_template('spells.html')


@app.route("/characters", methods=["GET"])
def characters():
    return render_template('characters.html')


@app.route("/positions", methods=["GET"])
def potions():
    return render_template('positions.html')


if __name__ == "__main__":
    app.run(debug=True)
