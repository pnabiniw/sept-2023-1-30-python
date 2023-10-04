# There are some built-in functions which can take tuple as an argument

# sum(iterable)
print(sum((4, 5, 6)))  # 15


# max() / min()
a = (4, 5, 6, 7)
print(max(a))  # 7
print(min(a))  # 4


# sorted()
a = (3, 2, 5, 1, 7, 4)
r = sorted(a)
print(r)  # [1, 2, 3, 4, 5, 7]
tuple(r)


# reversed()
a = (3, 2, 5, 1, 7, 4)
r = reversed(a)
print(list(r))  # [4, 7, 1, 5, 2, 3]
