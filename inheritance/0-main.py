#!/usr/bin/env python3

"""
Demonstarates class inheritance and the use of issubclass().

This script defines a hierarch of vehicle classes:
    - Vehicle (base class)
    - LandVehicle (inherits from Vehicle)
    - TrackedVehicle (inherits from LandVehicle)

It then iterates through all combinations of these classes to print
a matrix showing the results of issubclass() checks, illustrating
their inheritance relationship.
"""
class Vehicle:
    """
    A base class representing a generic vehicle.

    This class serves as the root of the vehicle inheritance hierarchy.
    """
    pass


class LandVehicle(Vehicle):
    """
    Represents a vehicle that operates on land.

    Inherits from Vehicle.
    """
    pass


class TrackedVehicle(LandVehicle):
    """
    Represents a land vehicle that uses tracks for locomotion.

    Inherits from LandVehicle.
    Example: A tank or a bulldozer.
    """
    pass

# ---nMain execution block ---
if __name__ == "__main__":
    """
    Iterates through the defined vehicle classes to demonstrate issubclass().

    This section prints a table where each cell (row, col) indicates
    whether cls1 (from rows) is a subclass of cl2 (from columns).
    """
    print("Issubclass check (cls1 is subclass of cls2?):")
    print("             Vehicle   LandVeh.    TrackedVeh.")
    class_list = [Vehicle, LandVehicle, TrackedVehicle]
    for cls1 in class_list:
        print(f"{cls1.__name__:<12}", end="") # Added for better readability
        for cls2 in class_list:
            print(issubclass(cls1, cls2), end="\t")
        print()
