# Tuples in python can be packed and unpacked


# Tuple Packing
a = 1,  # this is tuple packing
print(a)
a = 2, 3, 4   # This is also a tuple packing
print(a)

vowels = "a", "e", "i", "o", "u"
print(vowels)  # ("a", "e", "i", "o", "u")


# Tuple Unpacking
a, b, c = 2, 3, 4
print(a)  # 2
print(b)  # 3
print(c)  # 4


# Errors in tuple packing and unpacking
a, b = 2, 3, 4  # too many values to unpack
a, b, c = 1, 2  # not enough values to unpack


# Swapping two values in python

a = 1
b = 2

temp = a
a = b
b = temp

print(a)  # 2
print(b)  # 1


a = 1
b = 2
a, b = b, a
print(a)  # 2
print(b)  # 1
