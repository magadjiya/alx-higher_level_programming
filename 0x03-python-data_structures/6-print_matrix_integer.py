#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers

    Args:
        @matrix: 2D matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])

    for elem in range(rows):
        for elems in range(cols):
            print("{:d}".format(matrix[elem][elems]), end="")
            if elems < cols - 1:
                print(end=" ")
        print()
