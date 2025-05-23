#!/usr/bin/env python3

"""Talking to JSON in Python"""

# Interpreting Lists

import json

jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
my_list = json.loads(jstr)

print(type(my_list))
print(my_list)
