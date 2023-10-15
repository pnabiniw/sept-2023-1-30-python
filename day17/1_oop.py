# OOP is an approach of programming in which programs are modeled in the real world-problems
# OOP stands for Object-Oriented Programming
# It has two major aspects; Class and Objects
# Class is the blueprint of an object. It has its own attributes known as properties and methods
# Objects are the instance of a class

# There are four major pillars of OOP
# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. Abstraction


class Vehicle:
    engine_type = "petrol"  # class attribute

    def __init__(self, number_of_doors, color):  # Constructor
        self.number_of_doors = number_of_doors  # instance attribute
        self.color = color  # instance attribute

    def description(self):  # method
        return f"Vehicle has {self.number_of_doors} doors and {self.color} color"



v1 = Vehicle(4, "red")
print(v1.number_of_doors)  # 4
print(v1.color)  # red
print(v1.engine_type)  # petrol
print(v1.description())

print(Vehicle.engine_type)  # petrol
print(v1.engine_type)  # petrol


# print(Vehicle.color)  # Attribute Error because color is an instance attribute

# In this Vehicle class "engine_type" is a class attribute and color and number of doors are instance
# attributes and __init__() is a constructor
v1.number_of_doors = 2
print(v1.number_of_doors)  # 2
Vehicle.engine_type = 'diesel'
print(Vehicle.engine_type)  # "diesel"
print(v1.engine_type)  # petrol

