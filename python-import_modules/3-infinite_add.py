#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    result = 0
    for n in range(1, len(argv)):
        cast = int(argv[n])
        result += cast
    print("{}" .format(result))
