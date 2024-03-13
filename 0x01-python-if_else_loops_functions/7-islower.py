#!/usr/bin/python3

def islower(c):
    """
    This function checks for a lowercase character

    Args:
        c: the character to be checked

    Returns:
        True if c is lowercase, False if not
    """

    if ord(c) in range(97, 123):
        return True
    return False
