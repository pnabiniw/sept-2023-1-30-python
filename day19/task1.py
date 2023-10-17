"""
Create a class Department with parameters name and number_of_students.
Create a method total students, which takes department object as a parameter
and return the total number of students from all departments.

"""


class Department:
    def __init__(self, name, number_of_students):
        self.name = name
        self.number_of_students = number_of_students

    def get_total_students(self, other):
        return self.number_of_students + other.number_of_students


d1 = Department("CS", 40)
d2 = Department("IT", 30)
result = d2.get_total_students(d1)
print(result)  # 70
