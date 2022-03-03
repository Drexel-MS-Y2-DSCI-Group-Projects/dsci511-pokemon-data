from collections import Counter
import json

"""
This module exposes a function to query the merged data for specified keys and values.

Example usage:
    query(color="blue", types=['Fairy', 'Steel'])
"""
def query(**kwargs):
    with open("merged.json", "r") as f:
        data = json.load(f)

    for key, value in kwargs.items():
        data = dict(filter(lambda x: _filter(x, key, value), data.items()))

    return data

def _filter(element, key, value):
    if not key in element[1]:
        return False
    
    if type(element[1][key]) is list:
        return Counter(element[1][key]) == Counter(value)
    
    return element[1][key] == value
