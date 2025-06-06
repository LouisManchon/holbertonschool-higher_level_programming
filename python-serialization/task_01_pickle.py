#!/usr/bin/env python3
import pickle


class CustomObject:

    def __init__(self, name="", age=0, is_student=bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
