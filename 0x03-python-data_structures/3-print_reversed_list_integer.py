#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints a list in reverse

    Args:
        @my_list: the list to be printed in reverae
    """
    my_list.reverse()
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
