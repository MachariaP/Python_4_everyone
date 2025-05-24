#!/usr/bin/env python3

import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]

def show_head():
    """Prints the header row for a table displaying car data.

    Iterates through 'key_names' and 'key_widths' using 'zip()' to print each property name,
    left-justified to its specified width, followed by a '|' separator. A newline
    is printed to complete the header row.
    """
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()

def show_car(car):
    """Prints a single row of car data in a formatted table.

    iterates through 'key_names' and 'key_widths' using 'zip()' to access and print the
    value of each property from the provided 'car' dictionary, left-justified to its
    specified width, followed by a '|' separator. A newline is printed to
    complete the row.

    Args:
        car (dict): A dictionary containing car data with keys matching 'keys_names'.
    """
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()

def show(json):
    """Prints a formatted table of car data from a JSON list.

    Calls 'show_head()' to print the table header, then iterates through the provided JSON
    list, calling 'show_car()' for each car to print its data as a table row.

    Args:
        json(list): A list of dictionaries, each containing car data with keys matching
        'key_names'.
    """
    show_head()
    for car in json:
        show_car(car)
try:
    # Attempt to send a GET request to the local server endpoint for cars data
    reply = requests.get("http://localhost:3000/cars")
# Handle any network-related error (e.g., connection issues, timeouts)
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    else:
        # Handle non-200 status code (e.g., 404, 500)
        print("Server error")
