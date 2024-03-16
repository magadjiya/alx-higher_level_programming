#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Find and return the element at a given index

    Args:
        my_list: list yo go through
        @idx: element at index

    Return:
        the element if found, None if not
    """
    if idx < 0 or idx >= len(my_list):
        return (None)
    elem = my_list.pop(idx)
    return (elem)
