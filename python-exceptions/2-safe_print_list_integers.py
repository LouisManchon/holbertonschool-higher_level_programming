#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    elements_number = 0

    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elements_number += 1
        except (TypeError, ValueError):
            continue
    print()
    return elements_number
