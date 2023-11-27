import json
filename = 'students.json'


def read_student():
    student_id = input("Enter the student id ")  # 20
    with open(filename, 'r') as fp:
        data = json.loads(fp.read())  # [{id: 1, }, {id: 2}, {id: 20}]
    # for student in data:
    #     if student_id == student['id']:
    #         print(student)
    #         break
    student = list(filter(lambda x: x['id'] == student_id, data))  # [{id: 20}]
    if student:
        print(student[0])
    else:
        print("Please enter a valid student id")
    choice = input("Do you wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False

