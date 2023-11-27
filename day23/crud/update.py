import json
filename = 'students.json'


def update_student():
    student_id = input("Enter the student id ")
    to_change = input("Enter the field you want to change ")
    new_value = input(f"Enter the new {to_change}")

    with open(filename, "r+") as fp:
        data = json.loads(fp.read())  # [{}, {}, {}]
        student = list(filter(lambda x: x['id'] == student_id, data))  # [{}]
        if student:
            student = student[0]
            student[to_change] = new_value
            fp.seek(0)
            fp.write(json.dumps(data, indent=2))
            print("Info has been updated !!")
        else:
            print("Invalid student id")
    choice = input("Do you wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
