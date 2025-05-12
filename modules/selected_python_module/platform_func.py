#!/usr/bin/env python3

"""
The platform module lets you access the underlying platform's data,
i.e., hardware, operating system, and interpreter version information.
"""

from platform import platform, machine, processor, system, version

print("Platform:", platform())
print("Machine:", machine())
print("Processor:", processor())
print("System:", system())
print("Version:", version())
