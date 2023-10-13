# Decorators are the design pattern in python functions which add extra functionality to the
# existing function
# Closures are the fundamental to design a decorator

# Following are the criteria for the decorator
# 1. A function takes another function as an argument
# 2. The function includes another function definition (nested function)
# 3. Inner function calls the argument from the outer function and return
# 4. Outer function returns the inner function

def decorate_me(func):  # func => message
    def inner_func():
        print("This is the extra functionality")
        return func()  # "Hello World"
    return inner_func


@decorate_me
def message():
    return "Hello World"


# message = decorate_me(message)  # inner_func
print(message())
