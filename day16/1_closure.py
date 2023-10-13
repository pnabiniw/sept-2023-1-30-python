# Closure is a function based design pattern in python
# There are certain criteria to create a closure

# 1. A function must take object as an argument
# 2. The function must include another function definition (nested function)
# 3. The inner function must refer to the parameter in the outer function
# 4. Outer function must return the inner function


def closure_func(msg):
    def inner_func():
        print(msg)
    return inner_func


result = closure_func("Hello World")
result()  # Hello World

