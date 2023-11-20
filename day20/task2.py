class Department:
    def __init__(self, name, no_of_students):
        self.name = name
        self.no_of_students = no_of_students

    def total_students(self, other):
        return self.no_of_students + other.no_of_students

    def __add__(self, other):
        return self.no_of_students + other.no_of_students


d1 = Department("Civil", 30)
d2 = Department("IT", 25)
print(d1.total_students(d2))  # 55

print(d1 + d2)  # 55
