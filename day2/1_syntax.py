# Identifiers are the variables, function name, class name and python module name
# Any name of a variable, function or class provided by the user is an identifier

# Rules of naming identifiers in python
# 1. Identifiers are case-sensitive i.e. Area and area are two different variables
# 2. Identifiers can't be python keywords.
# 3. Identifiers name can have A-Z, a-z, 0-9 and _
# 4. But it can't start with digit. 1a = "hello". Here 1a is invalid identifier.
# 5. We can't use special symbols like @, $, # as identifiers.


# Python statement
# Each line of a python program is called a python statement
# A python statement can be written in multiple lines
# Each line of the program can also include multiple statements


a = 1; b = 2; print(a)
a = "Hello World. " \
    "I'm learning Python." \
    "Python is a high level language"
# We can use back-slash \, for the line continuation
import csv, \
    json, math


#### Indentation in Python ####
# Code blocks in python are separated by using indentation
# A indentation is equivalent to 1 tab or 4 spaces
# Functions, conditions, classes and loops can have their code blocks

# Code blocks in other languages (C, C++, Java etc.) are kept in curly braces {}
# For example
# a = 5
# if(a==5){
# print("The number is 5")
# }
# else{
# print("Number is something else")
# }

# Python is a dynamically typed language. We do not need to explicitly mention the type
# of variables and functions

a = 5
if a == 5:
    print("The number is 5")
else:
    print("The number is sth else")


a = 1
b = 2
if a == 1:
    print("Hello World")
    if b == 2:
        print("2 is also printed")
    print("This is outside b")
print("This is not in if code block")
