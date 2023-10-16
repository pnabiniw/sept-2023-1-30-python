# Multiple Inheritance

class A:
    p = 1

class B:
    q = 2

class C(A, B):
    r = 3

obj = C()
print(obj.r)
print(obj.p)
print(obj.q)


# Multilevel Inheritance
class A:
    p = 1


class B(A):
    q = 2


class C(B):
    r = None
    def add(self):
        self.r = self.p + self.q
        return self.r


obj = C()
print(obj.r)
print(obj.q)
print(obj.p)
obj.add()
print(obj.r)  # 3


# Hierarchical Inheritance
class A:
    p = 1

class B(A):
    q = 2

class C(A):
    r = 3



# Hybrid Inheritance

class A:
    p = 1

class B(A):
    q = 2


class C(A):
    r = 3

class D(B, C):
    x = 4

class E(D):
    y = 5


# MRO => It stands for Method Resolution Order
# MRO is an order in which the object of a class can access the attributes

obj = E()
# print(obj.a)
print(E.mro())

