from flask import Flask, render_template, request
import requests

BASE_URL = "https://pokeapi.co/api/v2/"
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        poke = request.form['pokemon']
        pokemon = get_pokemon_info(poke)
        name = pokemon['name']
        id = pokemon['id']
        height = pokemon['height']
        weight = pokemon['weight']
        info = {'name': name, 'id': id, 'height': height, 'weight': weight}
        return render_template("index.html", info=info)
    else:
        return render_template("index.html")


def get_pokemon_info(name):
    url = f"{BASE_URL}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        return json
    else:
        print(f"No pokemon found...")


if __name__ == "__main__":
    app.run(debug=True)
