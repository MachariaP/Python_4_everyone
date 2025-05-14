#!/usr/bin/env python3

"""
String Methods in Python
=======================
Python provides a rich set of built-in string methods for manipulating and inspecting strings.
Below is a comprehensive list of the 45 string methods available in Python 3.12, along with their descriptions.
Each method is demonstrated in the code below with a simple example.

1. capitalize() - Converts the first character to uppercase and the rest to lowercase.
2. casefold() - Converts the string to lowercase for case-insensitive comparisons (more aggressive than lower()).
3. center(width[, fillchar]) - Centers the string in a field of specified width, padded with fillchar (default is space).
4. count(sub[, start[, end]]) - Returns the number of non-overlapping occurrences of substring sub in the string.
5. encode(encoding='utf-8'[, errors='strict']) - Encodes the string into bytes using the specified encoding.
6. endswith(suffix[, start[, end]]) - Returns True if the string ends with the specified suffix.
7. expandtabs(tabsize=8) - Replaces tabs with spaces, using the specified tabsize.
8. find(sub[, start[, end]]) - Returns the lowest index of substring sub in the string; returns -1 if not found.
9. format(*args, **kwargs) - Formats the string using placeholders.
10. format_map(mapping) - Formats the string using a mapping (e.g., dictionary) for placeholders.
11. index(sub[, start[, end]]) - Like find(), but raises ValueError if substring sub is not found.
12. isalnum() - Returns True if all characters are alphanumeric and the string is non-empty.
13. isalpha() - Returns True if all characters are alphabetic and the string is non-empty.
14. isascii() - Returns True if all characters are ASCII (code points 0-127).
15. isdecimal() - Returns True if all characters are decimal digits (0-9) and the string is non-empty.
16. isdigit() - Returns True if all characters are digits and the string is non-empty.
17. isidentifier() - Returns True if the string is a valid Python identifier.
18. islower() - Returns True if all cased characters are lowercase and there is at least one cased character.
19. isnumeric() - Returns True if all characters are numeric (e.g., digits, Unicode numeric characters).
20. isprintable() - Returns True if all characters are printable or the string is empty.
21. isspace() - Returns True if all characters are whitespace and the string is non-empty.
22. istitle() - Returns True if the string is title-cased (each word's first character uppercase, rest lowercase).
23. isupper() - Returns True if all cased characters are uppercase and there is at least one cased character.
24. join(iterable) - Concatenates strings in the iterable, using the string as a separator.
25. ljust(width[, fillchar]) - Left-justifies the string in a field of specified width, padded with fillchar.
26. lower() - Converts all characters to lowercase.
27. lstrip([chars]) - Removes leading characters (default is whitespace) from the string.
28. maketrans(x[, y[, z]]) - Creates a translation table for use with translate().
29. partition(sep) - Splits the string at the first occurrence of sep, returning a tuple (before, sep, after).
30. replace(old, new[, count]) - Replaces occurrences of old with new, optionally up to count times.
31. rfind(sub[, start[, end]]) - Returns the highest index of substring sub; returns -1 if not found.
32. rindex(sub[, start[, end]]) - Like rfind(), but raises ValueError if substring sub is not found.
33. rjust(width[, fillchar]) - Right-justifies the string in a field of specified width, padded with fillchar.
34. rpartition(sep) - Splits the string at the last occurrence of sep, returning a tuple (before, sep, after).
35. rsplit([sep[, maxsplit]]) - Splits the string from the right using sep, up to maxsplit times.
36. rstrip([chars]) - Removes trailing characters (default is whitespace) from the string.
37. split([sep[, maxsplit]]) - Splits the string using sep, up to maxsplit times.
38. splitlines([keepends]) - Splits the string at line breaks, optionally keeping line endings.
39. startswith(prefix[, start[, end]]) - Returns True if the string starts with the specified prefix.
40. strip([chars]) - Removes leading and trailing characters (default is whitespace).
41. swapcase() - Swaps the case of each character (uppercase to lowercase and vice versa).
42. title() - Converts the first character of each word to uppercase, others to lowercase.
43. translate(table) - Returns a string with characters replaced or removed based on a translation table.
44. upper() - Converts all characters to uppercase.
45. zfill(width) - Pads the string on the left with zeros to reach the specified width, preserving signs.
"""

from colorama import init, Fore, Style
import sys

# Initialize colorama for cross-platform colored output
init()

# Sample string for demonstrations
text = "Hello, World!\nPython 3.12\tTest"

# Helper function to print with consistent formatting and colors
def print_method(method_name, result):
    print(f"{Fore.CYAN}{Style.BRIGHT}{method_name}{Style.RESET_ALL}: {Fore.GREEN}{result}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}")

# 1. capitalize()
print_method("capitalize()", text.capitalize())

# 2. casefold()
print_method("casefold()", text.casefold())

# 3. center()
print_method("center(20, '*')", text.center(20, '*'))

# 4. count()
print_method("count('o')", text.count('o'))

# 5. encode()
print_method("encode()", text.encode(encoding='utf-8'))

# 6. endswith()
print_method("endswith('Test')", text.endswith('Test'))

# 7. expandtabs()
print_method("expandtabs(4)", text.expandtabs(4))

# 8. find()
print_method("find('World')", text.find('World'))

# 9. format()
print_method("format()", "Hello, {}!".format("Alice"))

# 10. format_map()
print_method("format_map()", "Hello, {name}!".format_map({'name': 'Bob'}))

# 11. index()
print_method("index('Python')", text.index('Python'))

# 12. isalnum()
print_method("isalnum('Python312')", "Python312".isalnum())

# 13. isalpha()
print_method("isalpha('Python')", "Python".isalpha())

# 14. isascii()
print_method("isascii()", text.isascii())

# 15. isdecimal()
print_method("isdecimal('123')", "123".isdecimal())

# 16. isdigit()
print_method("isdigit('123')", "123".isdigit())

# 17. isidentifier()
print_method("isidentifier('my_var')", "my_var".isidentifier())

# 18. islower()
print_method("islower('hello')", "hello".islower())

# 19. isnumeric()
print_method("isnumeric('123')", "123".isnumeric())

# 20. isprintable()
print_method("isprintable()", text.isprintable())

# 21. isspace()
print_method("isspace('   ')", "   ".isspace())

# 22. istitle()
print_method("istitle('Hello World')", "Hello World".istitle())

# 23. isupper()
print_method("isupper('HELLO')", "HELLO".isupper())

# 24. join()
print_method("join(['a', 'b', 'c'])", "-".join(['a', 'b', 'c']))

# 25. ljust()
print_method("ljust(20, '*')", text.ljust(20, '*'))

# 26. lower()
print_method("lower()", text.lower())

# 27. lstrip()
print_method("lstrip('H')", text.lstrip('H'))

# 28. maketrans() and translate()
trans_table = str.maketrans('aeiou', '12345')
print_method("translate(maketrans)", "hello".translate(trans_table))

# 29. partition()
print_method("partition(',')", text.partition(','))

# 30. replace()
print_method("replace('World', 'Python')", text.replace('World', 'Python'))

# 31. rfind()
print_method("rfind('o')", text.rfind('o'))

# 32. rindex()
print_method("rindex('o')", text.rindex('o'))

# 33. rjust()
print_method("rjust(20, '*')", text.rjust(20, '*'))

# 34. rpartition()
print_method("rpartition(' ')", text.rpartition(' '))

# 35. rsplit()
print_method("rsplit(' ', 1)", text.rsplit(' ', 1))

# 36. rstrip()
print_method("rstrip('Test')", text.rstrip('Test'))

# 37. split()
print_method("split()", text.split())

# 38. splitlines()
print_method("splitlines()", text.splitlines())

# 39. startswith()
print_method("startswith('Hello')", text.startswith('Hello'))

# 40. strip()
print_method("strip('HT')", text.strip('HT'))

# 41. swapcase()
print_method("swapcase()", text.swapcase())

# 42. title()
print_method("title()", text.title())

# 43. translate()
print_method("translate()", text.translate(trans_table))

# 44. upper()
print_method("upper()", text.upper())

# 45. zfill()
print_method("zfill(20)", "42".zfill(20))
