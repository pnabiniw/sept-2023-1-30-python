# Polymorphism in Python refers to many forms of the same functions or objects
# sum(), len(), max(), min() etc. they are some of the examples which follows polymorphism.
# These built-in functions can take different datatypes and performs their respective tasks

# There are three important aspects of Polymorphism:
# 1. Function / Method Overloading
# 2. Operator Overloading
# 3. Method Overriding


# Function / Method Overloading
def add(a, b):
    return a + b

def add(a, b, c):  # Here this is function overloading and it is not supported in python
    return a + b + c

result1 = add(1, 2)
print(result1)  # 3

result2 = add(1, 2, 3)
print(result2)  # 6

# Python doesn't support function or method overloading
# If a function with same name is defined multiple times then only the latest definition is considered


class Student:
    name = "Ram"

    def display(self):
        return f"Name is {self.name}"

    def display(self):
        return f"Name of the student is {self.name}"

s = Student()
print(s.display())  # Name of the student is Ram
