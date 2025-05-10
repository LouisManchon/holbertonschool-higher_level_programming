#!/usr/bin/python3
def uppercase(str):
    for i in str:
        upper = ord(i)
        if 97 <= upper <= 123:
            upper -= 32
        print("{:c}" .format(upper), end="")
    print("")
