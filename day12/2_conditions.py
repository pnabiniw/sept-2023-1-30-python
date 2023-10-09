# Conditions are used to make decisions in a program
# There are five variations of conditions in python
# 1. Simple if
# 2. if...else
# 3. if...elif...else ladder
# 4. Nested if
# 5. ternary if

# 1. Simple if
# If conditions do not necessarily need True or False statement
# if conditions can take truthy or falsy statement

a = 3
b = 5
c = []
if b > a:
    print("b is greater")

if a:
    print("a is non-zero")

if c:
    print("c is non-empty")


# 2. if...else
a = 3
b = 5
c = []
if b > a:
    print("b is greater")
else:
    print("a is greater")

if a:
    print("a is non-zero")
else:
    print("a is zero")

if c:
    print("c is non-empty")
else:
    print("c is empty")


# 3. if...elif...else ladder
b = 10
if b == 2:
    print("the number is two")
elif b == 5:
    print("the number is 5")
elif b == 10:
    print("the number is 10")
else:
    print("There is no number")


# 4. Nested if
a = 5

if a < 10:
    if a == 5:
        print("The number is 5")
    else:
        print("Number is less than 10 but except 5")
else:
    print("the number is greater than 10")


# 5. Ternary if
a = 5
print("a is greater than 10") if a > 10 else print("a is less than 10")
