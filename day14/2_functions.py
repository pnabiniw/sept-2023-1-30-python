# Functions are the block of reusable codes
# 'def' keyword is used to define a function in Python

# This is function definition
def addition(a, b):  # a and b are parameters
    result = a + b
    return result


# this is function call
s = addition(3, 4)  # 3 and 4 are the arguments
print(addition(3, 4))  # 7
print(s)  # 7


def summation(a, b):
    result = a + b
    print(result)
    return

s = summation(3, 4)
print(summation(3, 4))  # None
print(s)  # None
