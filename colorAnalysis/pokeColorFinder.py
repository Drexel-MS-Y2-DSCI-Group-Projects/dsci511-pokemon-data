import colorAnalyzer
import json
import os

img_directory = "../img"


with open("../pokemondb/data/pokemon_data.json", "r") as f:
    pokemon_data = json.load(f)

for file in os.listdir(img_directory):
    full_path = os.path.join(img_directory, file)
    key = file.split(".")[0]

    if not key:
        continue
    
    colors = colorAnalyzer.get_hex_codes_for_img(path=full_path)

    try:
        pokemon_data[key]["colors"] = colors
    except KeyError:
        pass

with open("../pokemondb/data/pokemon_data_colors.json", "w") as f:
    json.dump(pokemon_data, f, indent=4)