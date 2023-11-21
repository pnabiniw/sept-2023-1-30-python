# There are broadly two types of errors in Python
# 1. Syntactic Error
# 2. Non-Syntactic Error

# Syntactic errors occur when you mess up with the grammar of the Python
# Examples: Unwanted spaces, Indentation Error, Missed commas or colons etc

# Non-syntactic errors can further be classified as follow:
# 1. TypeError
# 2. ValueError
# 3. IndexError
# 4. KeyError
# 5. ZeroDivisionError
# 6. ModuleNotFoundError
# 7. AttributeError
# 8. NameError


# 2 + "hello"  # TypeError
# int("hello")  # ValueError

# a = [1, 2, 3]
# print(a[10]  # IndexError
# print(a[-20]) # IndexError


student = {"name": "Jon", "age": 20}
# print(student["address"])  # KeyError

# roll = student["roll"]
roll = student.get("roll", 10)
print(roll)  # None


# 5 / 0   # ZeroDivisionError
# from json import mat  # ImportError

class Student:
    def __init__(self, age):
        self.age = age


s = Student("Ram")
print(s.age)  # Ram
print(s.name)  # AttributeError

a = [1, 2, 3]
a.appendd()  # AttributeError

a = 2
# print(b)   # NameError

