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

## Data pipeline
PokeAPI, bulbapedia, and pokemondb data must be fetched before `merge.py` can be executed. The order largely does not matter for the pokemon data from the web.

**However** color analysis is done specifically on pokemondb data, so that data must be fetched before doing color analysis.

`query.py` likewise can only be run after data has been collected.

## The Data
* Type
* Height
* Weight
* Primary colors
* Shape
* Sprites (list of images)

## Querying the data
Prerequisite: run `run.py`:

```.py
from query import query
print(query(color="blue", types=['Fairy', 'Steel']))
```
