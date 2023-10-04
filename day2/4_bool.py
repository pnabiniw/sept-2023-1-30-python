# Boolean are immutable datatypes in Python
# True and False are the boolean types
# True and False are also the keywords and can't be used as identifiers

# Operations that give boolean result

# Comparison Operations
a = 5
b = 2
print(b > a)  # False
print(a != b)  # True


# Logical Operations
a = 5
b = 2
c = 5
print(a > b and a == c)  # True
print(a > b and a != c)  # False
print(a > b or a != c)  # True
print(not a)  # False


# Membership Operation
print(2 in [1, 2, 3])  # True
print(5 not in [1, 2, 3])  # True
print(6 in [1, 2, 3])  # false


# Identity Operation
a = 1
b = 1
print(a is b)  # True

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False
print(a == b)  # True



############### Concept of Truthy and Falsy #############
# Truthy
# All the non-empty datatypes including non-zero numbers and True itself are the Truthy datatypes
# We use bool() function to check whether the object is Truthy or Falsy

a = 50
b = [1, 2, 3]
c = (1, 2, 3)
d = {1, 2, 3}
e = {"name": "Jon"}
f = "hello"
g = True

print(bool(a))  # True
print(bool(b))  # True
print(bool(c))  # True
print(bool(d))  # True
print(bool(e))  # True
print(bool(f))  # True
print(bool(g))  # True


if a:
    print("It is non-zero number")
else:
    print("It is a zero")


# Falsy
# All the empty datatypes including zero, None and False itself are the falsy datatypes

a = 0
b = 0.0
c = []
d = ()
e = {}
f = set()
g = ""
h = None
i = False

print(bool(a))  # False
print(bool(b))  # False
print(bool(c))  # False
print(bool(d))  # False
print(bool(e))  # False
print(bool(f))  # False
print(bool(g))  # False
print(bool(h))  # False
print(bool(i))  # False

if a:
    print("It is non-zero number")
else:
    print("It is a zero")




# Python boolean are the sub-class of python integer class where value of True is '1' and the value of False is '0'

a = True + True
print(a)  # 2

b = False * 70
print(b)  # 0
