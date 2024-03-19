#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the element  of a list at a given index

    Args:
        @my_list: the list
        @idx: the index of the element to be deleted

    Return:
        The modified list, or the original list if
        index is out of bounds or negative
    """
    if idx < 0 or idx >= len(my_list) or len(my_list) == 0:
        return (my_list)
    del my_list[idx]
    return (my_list)
