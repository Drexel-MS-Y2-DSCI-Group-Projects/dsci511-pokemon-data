import json

def run():
    bulbapedia_json_file = open('bulbapedia\data\output.json')
    bulbapedia_data = json.load(bulbapedia_json_file)

    pokeapi_json_file = open('pokeAPI\data\detailed_pokemon_species_FULL_v2.json')
    pokeapi_data = json.load(pokeapi_json_file)

    pokemondb_json_file = open('pokemondb\data\pokemon_data.json')
    pokemondb_data = json.load(pokemondb_json_file)

    num_pokemon = 906
    merged = {}
    for i in range(1, num_pokemon):
        formatted_index = str(i).zfill(3)
        merged[formatted_index] = {
            **pokeapi_data.get(formatted_index, {}),
            **pokemondb_data.get(formatted_index, {}),
            'sprites': [
                *bulbapedia_data.get(formatted_index, {}).get('sprites', []),
                *pokeapi_data.get(formatted_index, {}).get('sprites', []),
                *pokemondb_data.get(formatted_index, {}).get('sprites', []),
            ]
        }

    with open('merged.json', 'w') as f:
        json.dump(merged, f, indent=4)

    bulbapedia_json_file.close()
    pokeapi_json_file.close()
    pokemondb_json_file.close()

if __name__ == '__main__':
    run()
