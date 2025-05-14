#!/usr/bin/env python3

"""
String Methods in Python
=========================
Python provides a rich set of built-in methods for manipulating and
inspecting strings.
Below is a comprehensive list of the string methods with example
"""

# Sample string for demonstrations
text = "Hello, World! Python 3.12\tTest"

print("Sample:", text)

"""
1. capitalize():
    - Convert the first character to uppercase and the rest to lowercase.
"""
print("Capitalize():", text.capitalize())

"""
2. casefold():
    - Converts the string to lowercase for case-insensitive comparisons.
    - More aggressive than lower().
"""
print("casefold():", text.casefold())
