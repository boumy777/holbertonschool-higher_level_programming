#!/usr/bin/python3
"""This module provides a function to add two integers."""

def add_integer(a, b=98):
    """Adds two integers or floats after casting them to integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float), default is 98.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
