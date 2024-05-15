#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Prints the result obtained from dividing two integers

    Args:
        @a: the first integer
        @b: the second integer

    Return:
        The result, None if errors
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = "None"
    finally:
        print("Inside result: {}".format(result))
        return (result)
