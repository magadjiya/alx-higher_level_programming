#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements from two lists element by element.

    Args:
        @my_list_1: First list of elements.
        @my_list_2: Second list of elements.
        @list_length: Number of elements to divide.

    Returns:
        A new list with the results of the division.
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
