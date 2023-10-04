# Membership Operation ("in" and "not in")
# Membership in dictionary is checked in keys (not in values)
student = {"name": "Alex", "age": 30}
print("name" in student)  # True
print("Alex" in student)  # False

print("age" not in student)  # False
