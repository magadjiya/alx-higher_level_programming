#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Finds the common elements between 2 sets
    i.e their intersection

    Args:
        @set_1: first set
        @set_2: second set

    Return:
        Intersection of sets 1 and 2
    """
    common_elem = set_1.intersection(set_2)
    return (common_elem)
