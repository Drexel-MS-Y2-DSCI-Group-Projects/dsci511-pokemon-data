import requests
import json

POKEMON_DATA_PATH = "data/pokemon_data.json"

def get_pokemon_data(file_path = POKEMON_DATA_PATH):
    with open(file_path, "r") as f:
        return json.load(f)

def download_image(key, poke_data):
    if not poke_data["sprites"]:
        return None

    url = poke_data["sprites"][0]
    extension = url.split(".")[-1]
    filename = f"../img/{key}.{extension}"

    response = requests.get(url, stream=True)

    if response.status_code != 200:
        return None
        
    response.raw.decode_content = True

    with open(filename, "wb") as f:
        f.write(response.content)

def download_pokemon_images():
    data = get_pokemon_data()

    for key in data:
        download_image(key, data[key])

download_pokemon_images()
