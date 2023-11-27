import json
import os
filename = "students.json"


def create_student():
    id = input("Enter the id of the student ")
    name = input("Enter the name of the student ")
    age = input("Enter the age of the student ")
    address = input("Enter the address of the student ")
    student = dict(id=id, name=name, age=age, address=address)
    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            data = json.dumps([student], indent=2)
            fp.write(data)
    else:
        with open(filename, "r+") as fp:
            data = json.loads(fp.read())  # [{}, {}]
            data.append(student)
            fp.seek(0)
            fp.write(json.dumps(data, indent=2))
    print("Student Added Successfully !!")
    choice = input("Do you wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
