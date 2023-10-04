# We do string formatting using f-string

name = "Jon"
message = f"Hello I am {name}"
print(message)  # "Hello I am Jon"

name = "John Doe"
age = 23
message = f"Hello I am {name}. I am {age} years old"
print(message)  # Hello I am John Doe. I am 23 years old

# using format specifier (%s, %d, %f etc)
print('I am %s and I am %d years old' % (name, age))

# using .format() method
print('I am {}'.format(name))

