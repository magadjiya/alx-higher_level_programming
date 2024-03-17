#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at the given index

    Args:
        @my_list: the list
        @idx: the index of the element to be replaced
        @element: the new element to set at idx

    Return:
        The original list if negative index or out of range
        The modified list otherwise
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    my_list[idx] = element
    return (my_list)
