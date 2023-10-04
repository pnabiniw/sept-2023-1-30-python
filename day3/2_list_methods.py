# Methods are also a function but all the functions are not methods
# Those functions which are defined inside a class and must be called using the class
# object are the methods

# For example:
def addition():  # Function definition
    a = 2
    b = 3
    return a + b


result = addition()  # Function call => This is a normal function (not a method)
print(result)  # 5

a = [3, 2, 1, 5, 4, 10]
a.sort()  # Function call => sort() is a function which is called with object. So, this is called a method
print(a)


######################### List Methods ########################

# append()
a = [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]

# extend()
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]


# insert(index, value)
a = [1, 2, 4, 5, 6]
a.insert(2, 3)
print(a)  # [1, 2, 3, 4, 5, 6]

vowels = ["a", "e", "i", "u"]
vowels.insert(3, "o")  # ["a", "e", "i", "o", "u"]


# remove(value)
vowels = ["a", "e", "i", "o", "u"]
vowels.remove("e")
print(vowels)  # ["a", "i", "o", "u"]

# If we provide a value not present in the list then the remove() method raises error
# vowels.remove("A")

# pop(index:optional)
a = [1, 2, 3, 4, 5]
result = a.pop()
print(result)  # 5
print(a)  # [1, 2, 3, 4]
result = a.pop(1)
print(result)  # 2
print(a)  # [1, 3, 4]


# clear()
a = [1, 2, 3]
result = a.clear()
print(result)  # None
print(a)  # []


# index(value, start:optional, end:optional)
vowels = ["a", "e", "i", "o", "u"]
result = vowels.index("i")
print(result)  # 2

vowels = ["a", "e", "i", "o", "u", "a", "i", "a", "o", "a"]
result = vowels.index("a")
print(result)  # 0
result = vowels.index("a", 4, 8)
print(result)  # 5


# count()
vowels = ["a", "e", "i", "o", "u", "a", "i", "a", "o", "a"]
result = vowels.count("a")
print(result)  # 4


# reverse()
a = [5, 3, 1, 10, 2, 6]
a.reverse()
print(a)  # [6, 2, 10, 1, 3, 5]
