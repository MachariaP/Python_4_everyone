#!/usr/bin/env python3

def toggle_case_string():
    """
    Converts uppercase characters to lowercase and vice versa in the string 'abc123XYX',
    while leaving non-letter characters unchanged. Prints the result without adding a newline.

    Args:
        None

    Returns:
        None

    Example:
        Input string: 'abc123XYX'
        Output: 'ABC123xyx'
    """
    for ch in "abc123XYX":
        if ch.isupper():
            print(ch.lower(), end='')
        elif ch.islower():
            print(ch.upper(), end='')
        else:
            print(ch, end='')

toggle_case_string()
