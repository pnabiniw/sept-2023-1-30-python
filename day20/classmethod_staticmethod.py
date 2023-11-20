# Class methods are the methods which takes class as the first parameter rather than self
# Class method is created using @classmethod decorator

# Static methods are the methods which neither takes class nor self as a parameter. They are like
# a normal function which doesn't change the state of the class.
# Static method is created using @staticmethod decorator

# ClassMethod is mainly used in creating factory method
class Student:
    def __init__(self, age):
        self.age = age

    @classmethod
    def from_birth_year(cls, year):
        age = 2023 - year
        return cls(age)

    @staticmethod
    def classroom(year):
        return f"Student of bachelor {year} year"


s1 = Student(23)
print(s1.age)  # 23

s2 = Student.from_birth_year(2000)
print(s2.age)  # 23

print(s1.classroom(1))
print(s2.classroom(2))

