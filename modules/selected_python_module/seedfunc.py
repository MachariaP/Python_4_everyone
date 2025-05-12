#!/usr/bin/env python3

"""
The seed() function is able to directly set the generator's seed.
seed() - sets the seed with the current time.
seed(int_value) - sets the seed with the integer value int_value.
"""

from random import random, seed

seed(3)

for i in range(5):
    print(random())
