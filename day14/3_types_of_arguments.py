# There are three types of function arguments in python
# 1. Positional Arguments
# 2. Keyword / Default Arguments
# 3. Arbitrary Arguments (*args, **kwargs)


# 1. Positional Arguments
# They are the compulsory arguments to be passed in a function

def addition(a, b):  # here a and b are the positional arguments
    return a + b


print(addition(3, 4))  # 7


# 2. Keyword / Default Arguments

def addition(a, b, c=2):  # here c is a default parameter
    return a + b + c


result = addition(2, 3, 4)  # 9
result = addition(a=2, b=3, c=4)  # 9  here a, b and c are keyword arguments
result = addition(a=1, c=3, b=2)  # 6
result = addition(2, 3, c=5)  # 10
result = addition(2, 3)  # 7
