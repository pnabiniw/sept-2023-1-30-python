# Unlike list, tuple doesn't have methods like append(), sort(), remove(), pop() etc. because tuple is
# an immutable datatype. So, tuple has only two methods, count() and index()


# count()
a = (1, 2, 3, 2, 3, 3, 2, 2, 1, 2)
r = a.count(2)
print(r)  # 5


# index(value, start:optional, end:optional)
vowels = ("a", "e", "i", "o", "u")
r = vowels.index("o")
print(r)  # 3

vowels = ("a", "e", "i", "o", "u", "i", "o", "a", "e", "a")
r = vowels.index("e", 3, 9)
print(r)  # 8
