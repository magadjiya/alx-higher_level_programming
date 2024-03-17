#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Changes the value at idx in my_list to element
    without affecting the original list

    Args:
        @my_list: the original list
        @idx: index of element to change
        @element: the new element to set

    Return:
        The new_ list or the old one if idx
        is out of range or negative
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
