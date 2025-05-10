#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    length = len(argv) - 1
    if length > 0:
        if length > 1:
            print("{} arguments:" .format(length))
        else:
            print("{} argument:" .format(length))
        for n in range(1, len(argv)):
            print("{}: {}" .format(n, argv[n]))
    else:
        print("0 arguments.")
