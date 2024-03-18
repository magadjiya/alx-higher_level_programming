#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints all the integers in a list

    Args:
        @my_list: a list containing integers
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
