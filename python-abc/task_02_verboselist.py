#!/usr/bin/python3
class VerboseList(list)


    def append(self, item):
        super().append(item):
        print("Added [item] to the list.")

    def extend(self, iterable):
        super().extend(iterable):
        print("Extended the list with [x] items.")

    def remove(item):
        super().remove(item):
        print("Removed [item] from the list.")

    def pop(index):
        super().pop(index):
        print("Popped [item] from the list.")
