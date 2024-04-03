#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Looks through a list and substitues the
    value of search with replace

    Args:
        @my_list: the list
        @search: the element to look for
        @replace: the new element to put

    Return:
        The modified list
    """
    if my_list is None:
        return (None)

    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
