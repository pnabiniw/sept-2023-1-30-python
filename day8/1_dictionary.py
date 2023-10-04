# Dictionary is the mutable datatype in python
# It is the datatype with key-value pair enclosed in the curly braces

# Creating an empty dictionary
a = {}
print(a)  # {}
a = dict()  # using built-in function
print(a)  # {}


# Creating non-empty dictionary
a = {"name": "Jon", "age": 30}
print(a)  # {"name": "Jon", "age": 30}

a = dict(name="Jon", age=30)
print(a)  # {"name": "Jon", "age": 30}

a = {"first name": "Jon", "last name": "Doe"}  # this is correct
print(a)  # {"first name": "Jon", "last name": "Doe"}

# a = dict(first name="Jon", last name="Doe") this is incorrect
a = dict(first_name="Jon", last_name="Doe")  # We should connect words in underscore in keys


####### Accessing dictionary elements ##############
student = {"name": "Jane", "age": 30, "address": "KTM"}
address = student['address']  # a = [1, 2, 3, 4]  # a[3]
print(address)  # KTM
# print(student["roll_no"])  # KeyError

name = student.get("name")
print(name)  # Jane
print(student.get("roll_no"))  # None


# Adding and Updating Dictionary elements
student = {"name": "Jane", "age": 30, "address": "KTM"}
student["roll_no"] = 2
print(student)   # {"name": "Jane", "age": 30, "address": "KTM", "roll_no": 2}

student["name"] = "Alex"
print(student)  # {"name": "Alex", "age": 30, "address": "KTM", "roll_no": 2}

student.update({"email": "jane@email.com", "contact": 898909898})
print(student)  # {"name": "Alex", "age": 30, "address": "KTM", "roll_no": 2, "email": "jane@email.com",
#                 "contact": 898909898 }

student.update(email="jane@email.com", contact="9898909887")
print(student)


# Removing Dictionary Elements
student = {"name": "Alex", "age": 30, "address": "KTM", "roll_no": 2,
           "email": "jane@email.com", "contact": 898909898}

contact = student.pop("contact")
print(student)  # {"name": "Alex", "age": 30, "address": "KTM", "roll_no": 2, "email": "jane@email.com"}
print(contact)  # 898909898

key, value = student.popitem()  # ("email", "jane@email.com")
print(student)  # {"name": "Alex", "age": 30, "address": "KTM", "roll_no": 2}
print(key)  # "email"
print(value)  # "jane@email.com"

student.clear()
print(student)  # {}

del student
print(student)  # NameError


# Restriction in dictionary keys
# All the immutable objects can be used as a dictionary key
# There is no restriction in dictionary values

data = {1: "Jon", 4: "Doe"}  # Valid
print(data[4])  # "Doe"

data = {1.1: "Jon", 3.2: "Doe"}  # Valid
data = {[1, 2]: "Ram", "age": 30}  # Invalid
data = {(1, 2): "Ram", "age": 30}  # Valid
data = {(1, [2, 3]): "Ram", "ages": [30, 31]}  # Invalid
