# Each operator in Python has its own magic method / dunder method which is called when the operation is \
# carried out
# Magic methods in python are the special methods created by using double underscore.
# __add__(), __mul__(), __sub__(), __gt__() etc. are some examples of magic methods

a = 1  # Integer Object
b = 2  # Integer Object
print(a + b)  # 3
print(a.__add__(b))  # 3
print(a.__mul__(b))

# So, everytime an operation is carried out, a magic method is called.
# Magic methods are also called as dunder methods
