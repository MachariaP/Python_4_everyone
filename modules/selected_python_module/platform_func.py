#!/usr/bin/env python3

"""
The platform module lets you access the underlying platform's data,
i.e., hardware, operating system, and interpreter version information.
"""

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))
