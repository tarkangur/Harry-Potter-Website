import requests
from flask import Flask, render_template, redirect, url_for


ENDPOINT = "https://api.potterdb.com/v1/"

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/books", methods=["GET"])
def books():
    response = requests.get(f"{ENDPOINT}books")
    data = response.json()
    books = [book['attributes'] for book in data['data']]
    return render_template("books.html", books=books)


@app.route("/films", methods=["GET"])
def films():
    response = requests.get(f"{ENDPOINT}movies")
    data = response.json()
    films = [film['attributes'] for film in data['data']]
    return render_template('films.html', films=films)


@app.route("/spells", methods=["GET"])
def spells():
    spells = []
    for i in range(1, 5):
        response = requests.get(f"{ENDPOINT}spells?page[number]={i}")
        data = response.json()
        for spell in data['data']:
            spells.append(spell['attributes'])
    return render_template('spells.html', spells=spells)


@app.route("/characters", methods=["GET"])
def characters():
    characters = []
    for i in range(1, 51):
        response = requests.get(f"{ENDPOINT}characters?page[number]={i}")
        data = response.json()
        for character in data['data']:
            characters.append(character['attributes'])
    return render_template('characters.html', characters=characters)


@app.route("/potions", methods=["GET"])
def potions():
    potions = []
    for i in range(1, 3):
        response = requests.get(f"{ENDPOINT}potions?page[number]={i}")
        data = response.json()
        for potion in data['data']:
            potions.append(potion['attributes'])
    return render_template('potions.html', potions=potions)


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
