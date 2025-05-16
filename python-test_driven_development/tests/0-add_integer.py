#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        a = int(a)
    except (ValueError, OverflowError):
        raise

    try:
        b = int(b)
    except (ValueError, OverflowError):
        raise

    return a + b
