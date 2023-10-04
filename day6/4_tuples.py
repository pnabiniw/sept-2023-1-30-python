# Tuples are immutable data type. They are sequential datatype
# Elements in tuple are enclosed within parenthesis (small brackets)

# Creating an empty tuple
a = ()
print(a)
b = tuple()
print(b)


# Creating non-empty tuple
a = (1, 2, 3)
print(a)
# Tuple elements can be of any datatype
a = (1, 2, 3.4, "hello", [5, 6], (1, 2))
print(a)


a = 1
print(type(a))  # int

a = 1,
print(type(a))  # tuple
print(a)  # (1,)

a = (1,)
print(type(a)) # tuple

a = "hello",
print(a)  # tuple

