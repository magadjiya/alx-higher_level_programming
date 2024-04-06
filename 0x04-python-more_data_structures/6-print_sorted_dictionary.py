#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints the sorted items of a dictionary
    """
    sorted_dict = sorted(a_dictionary.items())

    for key, value in sorted_dict:
        print("{}: {}".format(key, value))
