# all() => all() is a built-in function in Python which takes iterable
# as a parameter
# If all the elements of the iterable are truthy then it returns True

data = [1, "a", 3.1]
print(all(data))  # True

print(all([1, "", 2.1]))  # False

student = {"name": "Jon", "age": 30}
print(all(student))  # True

data = {0: "Jon", 1: "30"}
print(all(data))  # False


# any() => any() is also a built-in function in Python that takes iterable as an argument
# If any one of the elements in the iterable is True then any returns True

print(any([1, "", 2.1]))  # True
print(any([1, "", 0]))  # True
print(any([[], "", 0]))  # False

student = {"name": "Jon", "age": 30}
print(any(student))  # True

data = {0: "Jon", "": "30"}
print(any(data))  # False
