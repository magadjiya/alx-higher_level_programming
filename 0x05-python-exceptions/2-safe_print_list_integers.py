#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers

    Args:
        @my_list: The list to print elements from
        @x: The number of elements to access in my_list

    Return:
        The real number of integers printed
    """
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            raise
    print()
    return (count)
