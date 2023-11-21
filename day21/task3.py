"""
Create a dictionary student with keys id, name, age, department.
Take an input from the user, which info (id, name, age or department)
he wants to access and print the result. Handle the possible exceptions.
"""

student = {"id": 2, "name": "Ram", "age": 24, "department": "CS"}
key = input("Enter the info you want to access ")
try:
    data = student[key]
except KeyError:
    print("No data available !!")
else:
    print(f"{key} of the student is {data}")
