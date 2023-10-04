# Concatenation (+)
a = (1, 2, 3)
b = (4, 5, 6)
result = a + b
print(result)  # (1, 2, 3, 4, 5, 6)


# Repetition / Broadcast (*)
a = (1, 2)
result = a * 3
print(result)  # (1, 2, 1, 2, 1, 2)


# Membership Operation ("in" and "not in")
result = 2 in (1, 2, 3)
print(result)  # True

result = 3 not in (1, 2, 3)
print(result)  # False

print(5 in (1, 2, 3))  # False
print(6 not in (1, 2, 3)) # True

