from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print(f"Bark")


class Cat(Animal):
    def sound(self):
        print(f"Meow")
