#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Updates the key in a dictionary with value
    If key doesnt already exist, creates one

    Args:
        @a_dictionary: the dictionary
        @key: the key
        @value: its value

    Return:
        The updated dictionary
    """
    if key in a_dictionary:
        a_dictionary[key] = value
        return (a_dictionary)
    a_dictionary[key] = value
    return (a_dictionary)
