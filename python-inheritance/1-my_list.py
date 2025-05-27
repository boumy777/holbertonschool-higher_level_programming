#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""

class MyList(list):
    """
    A subclass of list that adds a method to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying the original list.
        """
        print(sorted(self))

