#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list

    Args:
        @my_list: the list
        @x: the number of elements

    Return:
        The total number of elements printed
    """
    count = 0
    for elem in range(x):
        try:
            print(my_list[elem], end="")
            count += 1
        except IndexError:
            break
    print()
    return (count)
