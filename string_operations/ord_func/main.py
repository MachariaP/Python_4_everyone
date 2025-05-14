#!/usr/bin/env python3
"""
The ord() function returns the Unicode code point (an integer) of a single character.
It's the opposite of the chr() function, which converts integer back to character.

Input - Takes exactly one character.
      - Raises error if you pass more than one character.

Output - Rerurns an integer representing the Unicode code point of the character.
"""

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))  # prints 97
print(ord(char_2))  # prints 32
