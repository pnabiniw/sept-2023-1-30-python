# String is an immutable datatype in Python
# String is created using single(''), double("") or triple(""" / ''') quotes in python
# A single character enclosed in the quotes is also a string

# Creating an empty string
a = ''  # single quotes
b = ""  # double quotes
c = """
"""  # triple quotes
d = '''
'''  # triple single quotes
e = str()  # using str() function


# Creating non-empty string
a = "Hello"
b = 'World'
c = """
I am Learning Python.
Python is a high level language
"""
print(c)


d = '''
I am Learning Python.
Python is a high level language
'''

# We can't start with one quote and end with another quote in strings
# a = 'Hello World"  # This is wrong

a = 'Hello World. I\'m learning python'
# '\ is an escape sequence

b = "Hello\nWorld"  # \n is an escape sequence
print(b)

c = "Hello\tWorld"  # \t escape sequence
print(c)
