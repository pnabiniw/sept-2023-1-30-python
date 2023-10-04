# Codes written in high level language must be converted into machine language.
# Compiler or Interpreter converts the high level language to machine language
# Compiler converts the whole program into the object code which is again converted to the machine code
# But, interpreter converts the program to machine code line by line
# Python is an interpreted, high-level, multi-purpose programming language


# Operators in Python
# Symbols which are used to perform the logical and arithmetic operations are called operators
# Like in any other language python also has its set of operators
# Python operators are:

# 1. Arithmetic Operators
# 2. Logical Operators
# 3. Relational / Comparison operators
# 4. Assignment Operators
# 5. Membership Operators
# 6. Identity Operators


# Arithmetic Operators
# 1. Addition (+)
a = 2
b = 1
c = a + b  # Here '+' is an addition operator
print(c)


# 2. Subtraction (-)
a = 5
b = 2
r = a - b  # Here '-' is a subtraction operator
print(r)


# 3. Multiplication (*)
a = 2
b = 2
r = a * b  # Here '*' is the multiplication operator
print(r)


# Division (/)
a = 2
b = 2
r = a / b  # Here '/' is the division operator
print(r)


# Power (**)
a = 4
r = a ** 2  # Here "**" operator raised power 2
print(r)


# Modulus Operator (%)
b = 4
r = b % 2  # Here % is the modulus operator
print(r)  # 0


# Floor Division (//)
a = 3
r = a // 2
print(r)  # 1


# Assignment Operator (=)
# "=" is the basic assignment operator. But, besides this +=, -=, *= etc are also the assignment operator

a = 1  # Here = is an assignment operator
a = a + 1
print(a)  # 2

a += 1
print(a)  # 3

a *= 3
print(a)  # 9


# Comparison / Relational Operators
# >, <, >=, <=, !=, == are the relational operators
# Result of the relational operation is either True or False
a = 5
b = 2
c = 5
print(a > b)  # True
print(a < b)  # False
print(a != b)  # True
print(a == b)  # False
print(a <= b)  # False
print(a >= c)  # True


# Logical Operators
# and, or, not are the logical operators
# Result of logical operation is also True / False
a = 5
b = 2
c = 5

print(a > b or c != b)  # True
print(a > b and c != b)  # True
print(a > b and c == b)  # False
print(a > b and a == c)  # True

print(not a)  # False
b = 0
print(not b)  # True


# Membership Operator
# 'in' and 'not in' are the membership operators
# Result of the membership operator is also in True / False

vowels = ["a", "e", "i", "o", "u"]
print("a" in vowels)  # True
print("h" in vowels)  # False
print("h" not in vowels)  # True
print("u" in vowels)  # True


# Identity Operator
# 'is' and 'is not' are the identity operators
a = 1
b = 1
print(a is b)  # True. Here both 'a' and 'b' are in the same memory location
print(id(a))
print(id(b))   # If identity of objects is same then, there 'id' is also same

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False
print(a is not b)  # True

a = None
b = None
print(a is b)  # True
# None type in python has always the same memory location. So, they always have the same identity
