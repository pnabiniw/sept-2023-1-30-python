# *args and **kwargs are the arbitrary arguments
# These arguments can take random number of parameters as input to the function

def addition(*args):
    print(args)
    print(type(args))
    return sum(args)


print(addition(1, 2))  # 3
print(addition(1, 2, 3))  # 6
print(addition(1, 2, 3, 4))  # 10


def summation(**kwargs):
    print(kwargs)  # {"a": 1, "b": 2}}
    values = kwargs.values()
    return sum(values)


print(summation(a=1, b=2))  # 3
print(summation(a=1, b=2, c=3))  # 6
print(summation(a=1, b=2, c=3, d=4))  # 10

