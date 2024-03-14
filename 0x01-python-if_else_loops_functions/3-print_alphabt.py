#!/usr/bin/python3

# ASCII lowercase letters without e and q
for char in range(97, 123):
    if char == 101 or char == 113:
        continue
    print("{}".format(chr(char)), end="")
