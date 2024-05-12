#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes an existing key in a dictionary

    Args:
        @a_dictionary: the dictionary
        @key: the key to be deleted

    Return:
        The updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
        return (a_dictionary)
    return (a_dictionary)
