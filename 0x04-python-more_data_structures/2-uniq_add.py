#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds unique integers in a list
    i.e dont add a specific number
    more than once

    Args:
        @my_list: the list

    Return:
        Sum of unique integers in given list
    """
    total = 0
    uniq_list = list(set(my_list))

    for num in range(len(uniq_list)):
        total = total + uniq_list[num]
    return (total)
