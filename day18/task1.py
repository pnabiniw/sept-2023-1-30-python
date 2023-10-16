class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name is {self.name} and age is {self.age}"


class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):
        print(super().get_details())
        return f"Salary is {self.salary} and designation is {self.designation}"


e1 = Employee("jon", 30, 30000, "Officer")
print(e1.get_details())
