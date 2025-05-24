#!/usr/bin/env python3

import requests

try:
    # Attempt to send a GET request to the local server endpoint for cars data
    reply = requests.get("http://localhost:3000/cars")
# Handle any network-related error (e.g., connection issues, timeouts)
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.headers['Content-Type'])
        print(reply.json())
    else:
        # Handle non-200 status code (e.g., 404, 500)
        print("Server error")
