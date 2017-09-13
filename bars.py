import json
import sys
from functools import reduce


def load_data(filepath):
    with open (filepath, 'r', encoding="utf-8") as current_json:
        return json.load(current_json)


def get_biggest_bar(data):
    d = {}
    [d.update({i.get("properties").get("Attributes").get("SeatsCount"): i}) for i in data.get("features")]
    return d.get(max(list(d.keys())))



def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    current_json = load_data(sys.argv[1])
    print(get_biggest_bar(current_json))


