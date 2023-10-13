# Create a login_required decorator which asks the user for password. If the password "123" is
# provided then the main function should be executed else print the message "Invalid Password"

def login_required(func):
    def inner_func():
        pw = input("Enter password ")
        if pw == "123":
            return func()
        else:
            return "Invalid Password"
    return inner_func


@login_required
def message():
    return "Hello World"


result = message()
print(result)
