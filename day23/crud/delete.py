import json
filename = "students.json"


def delete_student():
    student_id = input("Enter the student id ")
    with open(filename, "r") as fp:
        data = json.loads(fp.read())  # [{}, {}, {}]
    student = list(filter(lambda x: x["id"] == student_id, data))  # [{}]
    if student:  #
        student = student[0]  # {}
        data.remove(student)
        with open(filename, "w") as fp:
            fp.write(json.dumps(data, indent=2))
        print("Student deleted successfully !!")
    else:
        print("Invalid student id")
    choice = input("Do you wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
