import requests
from flask import Flask, render_template


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
    response = requests.get(f"{ENDPOINT}spells")
    data = response.json()
    spells = [spell['attributes'] for spell in data['data']]
    return render_template('spells.html', spells=spells)


@app.route("/characters", methods=["GET"])
def characters():
    response = requests.get(f"{ENDPOINT}characters")
    data = response.json()
    characters = [character['attributes'] for character in data['data']]
    return render_template('characters.html', characters=characters)


@app.route("/positions", methods=["GET"])
def potions():
    response = requests.get(f"{ENDPOINT}potions")
    data = response.json()
    potions = [potion['attributes'] for potion in data['data']]
    return render_template('positions.html', potions=potions)


if __name__ == "__main__":
    app.run(debug=True)
