"""

Inheritance:


Class A ---> Base Class  / Parent Class - Single level Inheritance

    def add(self):

Class B ---> Derived Class / Child Class


so from Inheritance we can access members, properties and methods from the another class

A <--- B <--- C - MultiLevel Inheritance

A    B --> Multiple Inheritance

  C

"""
# when there are 2 functions with same name in different classes, while using multiple inheritance,
# Which ever class comes first in the hierarchy, that class function is called.
# Here in the below example class Mamals(AnimalParent,Animal): the AnimalParent class comes first,
# so the hello function from AnimalParent class is called
class AnimalParent:
    def ap(self):
        print("Inside the Animal Parent class")

    def hello(self):
        print("Hello from Animal Parent class")


class Animal:
    name = "Rahul"
    def a(self):
        print("I am inside Animal class")

    def hello(self):
        print("Hello from Animal class")


class Mamals(AnimalParent,Animal):
    def b(self):
        print("I am inside Mamals class")


mam = Mamals()
mam.b()
mam.a()
print(mam.name)
mam.ap()
mam.hello()
