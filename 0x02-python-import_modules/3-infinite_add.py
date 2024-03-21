#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    summation = 0

    if argc == 1:
        print("{:d}".format(argc - 1))
    else:
        for arg in range(1, argc):
            summation += int(sys.argv[arg])
        print("{:d}".format(summation))
