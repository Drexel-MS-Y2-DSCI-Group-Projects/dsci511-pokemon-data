import colorAnalyzer
import json
import os
from pprint import pprint

img_directory = "../img"


with open("../pokemondb/data/pokemon_data.json", "r") as f:
    pokemon_data = json.load(f)

for file in os.listdir(img_directory):
    full_path = os.path.join(img_directory, file)

    colors = colorAnalyzer.get_hex_codes_for_img(path=full_path)

    
