#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Multiples all values in a dictionary by 2

    Args:
        @a_dictionary: the dictionary

    Return:
        The updated dictionary
    """
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return (new_dictionary)
