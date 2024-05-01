#!/usr/bin/python3

def uppercase(string):
    for char in string:
        if char.islower():
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()
