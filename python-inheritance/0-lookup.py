#!/usr/bin/python3
"""
This module defines the lookup function.
"""

def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the attributes and methods.
    """
    return dir(obj)

