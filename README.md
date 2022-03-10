## Pokemon Dataset
dsci511-pokemon-data contains a data acquisition pipeline for fetching physical traits of pokemon from various data aggregation sources.

## Getting Started
Prerequisite: Python 3

### Running the project
1. `python -m pip install -r requirements.txt`
2. `python run.py`

### Dependency highlights

**pandas**

For representing html table data to convert to json. Used in bulbapedia scraping.

**opencv-python**

For modifying image data during color parsing. We reshape scraped images and convert to RGB color space.

**scikit-learn**

We use k-Means clustering algorithm to find the top colors of a pokemon image, provided by the scikit learn library.

**numpy**

For representing image data as higher performance arrays during image decoding and color picking.

**beautifulsoup4**

For scraping all relevant data from each of our data sources.

**lxml**

This subdependency is required for the pandas read_html function to convert html tables into DataFrames.

### Standard library dependencies

**json**

JSON is our data format of choice. In intermediate steps it contains each module's data. This is how our final data is also stored.

**requests**

Capturing html from the web. Stringified HTML must be passed to BeautifulSoup.

**time**

Timing the runner provides additional insight during runs for the data scraping process.

**re**

Regex helps parse tables during bulbapedia scraping only containing pokemon data.

**getopt**

Command line parser tool for simplifying the query input processing.

## Sources
- [PokeAPI](https://pokeapi.co/docs/v2)
- [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number)
- [PokemonDB](https://pokemondb.net/pokedex/all)

## Data pipeline
PokeAPI, bulbapedia, and pokemondb data must be fetched before `merge.py` can be executed. The order largely does not matter for the pokemon data from the web.

**However** color analysis is done specifically on pokemondb image data, so that data must be fetched before doing color analysis. This was done only on the main official image for each Pokemon, since doing color analysis on each image was proving to be too intensive (but could be done by another user if required).

`query.py` likewise can only be run after all data has been collected and is available in merge.json.

## The Data
* Type
* Height
* Weight
* Primary colors
* Shape
* Sprites (list of images)

## Querying the data
Prerequisite: run `run.py`:

### Import the module

```.py
from poke_query import query
print(query(color="blue", types=['Fairy', 'Steel']))
```

### Execute in CLI

`python poke_query.py --name=pikachu`


## Some notes
- Currently, Shape data for the Pokemon after index 808 is missing, since that is pulled from PokeAPI and they have accidentally wiped it. In future runs, this data will most likely be back.
- Color analysis was not done on all images due to a timing constraint, but if needed someone could do this themselves.
- If any ML is wanting to be done on this data, it might not be enough. Most likely, will need to pull from additional sources in the future (such as Serebii, Pokemon.com and more)
