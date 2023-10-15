# Inheritance is the process of accessing the attributes in a Parent class by children classes
# Types of inheritance in Python
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


class A:
    p = 2


class B(A):  # This is inheritance
    q = 3


obj = B()
print(obj.q)  # 3
print(obj.p)  # 2

