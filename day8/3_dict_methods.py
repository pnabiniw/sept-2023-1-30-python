# get()
student = {"name": "Jon", "age": 30}
name = student.get("name")
print(name)  # "Jon

address = student.get("address", "PKR")
print(address)  # PKR

name = student.get("name", "Alex")
print(name)  # "Jon"


# keys()
student = {"name": "Jon", "age": 30, "address": "KTM"}
print(student.keys())  # dict_keys(["name", "age", "address"])


# values()
print(student.values())  # dict_values(["Jon", 30, "KTM"])


# items()
items = student.items()
print(items)  # dict_items([("name", "Jon"), ("age", 30), ("address", "KTM")])

for key, value in items:
    print(key)  # name
    print(value)  # Jon


a = int(input("Enter a number "))
