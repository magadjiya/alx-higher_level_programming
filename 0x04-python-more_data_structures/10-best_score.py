#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the person with the highest score in a dictionary

    Args:
        @a_dictionary: The dictionary to check through

    Return:
        The key with the highest value
    """
    if a_dictionary is None:
        return (None)

    # Set max to negative infinity to tackle negatives
    max_value = float('-inf')
    max_key = None
    for key, value in a_dictionary.items():
        if value > max_value:
            mmax_value = value
            max_key = key
    return (max_key)
