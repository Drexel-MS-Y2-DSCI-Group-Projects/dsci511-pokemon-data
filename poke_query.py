import getopt
import json
import sys

# Only these fields listed here can be queried.
QUERYABLE = {"name": str, "color": str, "shape": str, "types": list}

"""
This module exposes a function to query the merged data for specified keys and values.
Write now, queryable fields are name, color, shape, and types. When searching for types,
Pokemon with at least the types listed will be returned

Example usage:
    from poke_query import query
    query(color="blue", types=['Fairy', 'Steel'])

CLI Usage:
    python query.py --name=pikachu
    python query.py --types=Fairy,Steel
"""
def query(merged_path="merged.json", **kwargs):
    with open(merged_path, "r") as f:
        data = json.load(f)

    for key, value in kwargs.items():
        data = dict(filter(lambda x: _filter(x, key, value), data.items()))

    return data

def _filter(element, key, value):
    if not key in element[1]:
        return False
    
    if type(element[1][key]) is list:
        element_set = set(element[1][key])
        test_set = set(value)
        return len(element_set.intersection(test_set)) == len(test_set)
    
    return element[1][key] == value

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "p:", [opt + "=" for opt in QUERYABLE])
    query_args = { }

    for opt, arg in opts:
        opt_name = opt.strip('-')
        
        if opt == "p":
            query_args["merged_path"] = arg
            continue

        if QUERYABLE[opt_name] is list:
            query_args[opt_name] = arg.split(',')
        else:
            query_args[opt_name] = arg

    print(str(query(**query_args)))
