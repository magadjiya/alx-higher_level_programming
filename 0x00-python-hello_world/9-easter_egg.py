#!/usr/bin/python3
f = open("python.txt", "r")

for line in f:
    print(line, end="")

f.close()
