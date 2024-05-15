#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer using f-strings for formatting.

    Args:
        @value: The integer value to be printed.

    Return:
        True if value is integer, False if not
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
