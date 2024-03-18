#!/usr/bin/python3

def no_c(my_string):
    """
    Program that takes a string and removes all instances
    of c and C in it with the help of list comprehensions

    Args:
        @my_string: the string to modify
    """
    new_string = list(my_string)
    m_string = [i for i in new_string if i != 'C' and i != 'c']
    return (''.join(m_string))
