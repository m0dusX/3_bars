import json
import sys
from geopy.distance import vincenty


def show_info(bar):
    print(json.dumps(bar, indent=4, sort_keys=True, 
        ensure_ascii=False) + "\n")


def get_seatscount(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def load_data(filepath):
    with open (filepath, "r", encoding="utf-8") as current_json:
        return json.load(current_json)["features"]


def get_biggest_bar(all_bar_info):
    minimum = get_seatscount(max(all_bar_info, 
    	key=lambda bar: get_seatscount(bar)))
    #В списке баров может быть несколько баров с максимальным числом мест,
    #поэтому проверяем это и возвращаем список баров.
    all_biggest_bars = [bar for bar in all_bar_info 
        if get_seatscount(bar) == minimum]
    return all_biggest_bars


def get_smallest_bar(all_bar_info):
    bars_with_seats = [bar for bar in all_bar_info if get_seatscount(bar) > 0]
    minimum = get_seatscount(min(bars_with_seats, 
    	key=lambda bar: get_seatscount(bar)))
    #В списке баров может быть несколько баров с минимальным числом мест,
    #поэтому проверяем это и возвращаем список баров.
    all_smallest_bars= [bar for bar in all_bar_info
        if get_seatscount(bar) == minimum]
    return all_smallest_bars


def get_closest_bar(all_bar_info, longitude, latitude):
    closest_bar = min(all_bar_info, key=lambda bar: 
    	vincenty((longitude, latitude), (bar["geometry"]["coordinates"][0], 
            bar["geometry"]["coordinates"][0])).miles)
    return closest_bar


if __name__ == '__main__':
    current_json = load_data(sys.argv[1])
    print("Biggest bars in JSON:")
    for idx, current_bar in enumerate(get_biggest_bar(current_json), 1):
        print("{} bar:".format(idx))
        show_info(current_bar)
    print("Smallests bars in JSON:")
    for idx, current_bar in enumerate(get_smallest_bar(current_json), 1):
        print("{} bar:".format(idx))
        show_info(current_bar)
    longitude = float(input("Please enter longitude: "))
    latitude = float(input("Please enter latitude: "))
    print("Closest bar was found!")
    show_info(get_closest_bar(current_json, longitude, latitude))
    sys.exit()
