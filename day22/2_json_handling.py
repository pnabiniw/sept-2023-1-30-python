# JSON stands for JavaScript Object Notation
# JSON is a file format with .json extension which is used to share data and information over the
# internet
# Python has a built-in module for json handling
# JSON is similar to python dictionary as it is also written in key-value format. But, keys and values
# in JSON data must be enclosed in double-quotes. Single quotes are not allowed

# Integers and float values do not require quotes in JSON

# Some examples of JSON data
{"name": "Hary", "age": 30, "address": "KTM"}  # Valid JSON
{'name': 'Hary', 'age': 30, 'address': 'KTM'}  # Invalid JSON because of the single quotes

[
    {"name": "Hary", "age": 30, "address": "KTM"},
    {"name": "Jon", "age": 25, "address": "PKR"}
]   # Valid JSON

import json
filename = "student.json"
student = {'name': 'Jane', "age": 30, "address": "KTM"}
# loads and dumps are used to read and write json data to a json file in python

with open(filename, "w") as fp:
    data = json.dumps(student)
    fp.write(data)

with open(filename, "r") as fp:
    data = json.loads(fp.read())
    print(data)  # {"name": "Jane", "age": 30, "address": "KTM"}
print(type(data))  # str
print(data["age"])


students = [
    {"name": "Jon", "age": 23, "address": "KTM"},
    {"name": "Jane", "age": 25, "address": "PKR"},
    {"name": "Raj", "age": 21, "address": "BKT"}
]
filename = "students.json"
with open(filename, "w") as fp:
    data = json.dumps(students, indent=2)
    fp.write(data)

with open(filename, "r") as fp:
    data = json.loads(fp.read())
print(data)
print(type(data))  # list

name = students[2]["name"]
print(f"The name of the student is {name}")
