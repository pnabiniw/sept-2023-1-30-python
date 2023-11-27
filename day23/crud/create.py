import json
filename = "students.json"


def create_student():
    id = input("Enter the id of the student ")
    name = input("Enter the name of the student ")
    age = input("Enter the age of the student ")
    address = input("Enter the address of the student ")

    student = dict(id=id, name=name, age=age, address=address)
    with open(filename, "w") as fp:
        data = json.dumps(student, indent=2)
        fp.write(data)
    print("Student Added Successfully !!")
