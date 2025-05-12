#!/usr/bin/env python3

"""The most general function named random().
    Produces a float number x coming from the range (0.0, 1.0).
    In other words: (0.0 <= x < 1.0)
"""
from random import random

for i in range(5):
    print(random())
