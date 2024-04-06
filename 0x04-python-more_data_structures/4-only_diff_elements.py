#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns the elements of set_1 and set_1
    without the intersecting elements

    Args:
        @set_1: first set
        @set_2: second set

    Return:
        The symmetric differnce of sets 1 and 2
    """
    diff_elems = set_1.symmetric_difference(set_2)
    return (diff_elems)
