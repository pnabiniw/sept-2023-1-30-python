# Create a decorator function which capitalizes the return of the main function

def upper_case(func):  # decorator function
    def inner_func():
        return func().upper()
    return inner_func


@upper_case
def message():  # Original Function
    return "hello world"


result = message()
print(result)  # hello world  / HELLO WORLD
