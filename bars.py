import json
import sys
from geopy.distance import vincenty


def show_info(bar):
    print(json.dumps(bar, indent=4, sort_keys=True, 
        ensure_ascii=False) + "\n")

def get_seatscount(bar):
    return bar.get("properties").get("Attributes").get("SeatsCount")

def load_data(filepath):
    with open (filepath, "r", encoding="utf-8") as current_json:
        return json.load(current_json).get("features")

def get_biggest_bar(all_bar_info):
    """Return the biggest bar dict from list

    Uses lambda function to get SeatsCount for every bar as key argument in 
    max function & checks if there are more than one bars with max SeatsCount.

    """
    get_seatscount_lambda = lambda bar: get_seatscount(bar)
    minimum = get_seatscount(max(all_bar_info, key=get_seatscount_lambda))
    all_biggest_bars = [bar for bar in all_bar_info 
        if get_seatscount(bar) == minimum]
    return all_biggest_bars

def get_smallest_bar(all_bar_info):
    """Return the smallest bar dict from list

    At first, all bars with zero SeatsCount are excluded from the list. Then 
    lambda function is used to get SeatsCount for every bar as key argument in 
    min function & checks if there are more than one bars with min SeatsCount.

    """
    bars_with_seats = [bar for bar in all_bar_info if get_seatscount(bar) > 0]
    get_seatscount_lambda = lambda bar: get_seatscount(bar)
    minimum = get_seatscount(min(bars_with_seats, key=get_seatscount_lambda))
    all_smallest_bars= [bar for bar in all_bar_info
        if get_seatscount(bar) == minimum]
    return all_smallest_bars

def get_closest_bar(all_bar_info, longitude, latitude):
    """Return the closest bar dict from list

    Uses vincenty function from geopy.distance module in lambda function to
    calculate distance from user coordinates to current bar from all_bar_info
    list.

    """
    vincenty_lambda = lambda bar: vincenty((longitude, latitude), 
        (bar.get("geometry").get("coordinates")[0], 
            bar.get("geometry").get("coordinates")[0])).miles
    closest_bar = min(all_bar_info, key=vincenty_lambda)
    return closest_bar

if __name__ == '__main__':
    current_json = load_data(sys.argv[1])
    print("Biggest bars in JSON:")
    for idx, current_bar in enumerate(get_biggest_bar(current_json), 1):
        print("{} bar:".format(idx))
        show_info(current_bar)
    print("Smallest bar in JSON:")
    for idx, current_bar in enumerate(get_smallest_bar(current_json), 1):
        print("{} bar:".format(idx))
        show_info(current_bar)
    longitude = float(input("Please enter longitude: "))
    latitude = float(input("Please enter latitude: "))
    print("Closest bar is found!")
    show_info(get_closest_bar(current_json, longitude, latitude))
    print("Press enter to exit the programm...")
    input()
