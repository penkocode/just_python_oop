from abc import ABC, abstractmethod


# Abstraction
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    # Encapsulation
    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError('Name should be at least 3 chars')

    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        return "Meow!"


# Inheritance(common validators)
class Dog(Animal):
    def sound(self):
        return "Bow!"


# Polymorphism
for animal in Cat('Tom'), Dog('Frank'):
    print(animal.sound())
