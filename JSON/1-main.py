#!/usr/bin/env python3

import json

class Who:
    """A simple class to represent a person with a name and age.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    """

    def __init__(self, name, age):
        """Initialize a WHo instance with a name and age.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    """A custom JSON encoder to serialize who objects.

    This class extends json.JSONEncoder to handle serialization of who objects
    by converting them to their dictionary representation.
    """
    def default(self, w):
        """Convert a who object to a JSON-serializable format.

        Args:
            w: The object to serialize.

        Returns:
            dict: The dictionary representation of a who object if the input
                  is a Who instance.

        Raises:
            TypeError: If the object is not a who instance and cannot be
                       serialized by the default encoder.
        """
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(w)

some_man = Who('John Doe', 42)
print(json.dumps(some_man, cls=MyEncoder))
