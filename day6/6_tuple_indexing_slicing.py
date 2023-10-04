# Tuple elements can be accessed using indexing and slicing
# Indexing and slicing in tuple are similar to that of list and string

# Indexing
vowels = ("a", "e", "i", "o", "u")

print(vowels[4])  # "u"
print(vowels[0])  # "a"
print(vowels[-1])  # u
print(vowels[-3])  # i
print(vowels[10])  # error
print(vowels[-10])  # error


# slicing
data = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
print(data[:5])  # ("a", "b", "c", "d", "e")
print(data[0:7])  # ("a", "b", "c", "d", "e", "f", "g")
print(data[3:])  # ("d", "e", "f", "g", "h", "i", "j")
print(data[4:8])  # ("e", "f", "g", "h")
print(data[9:3])  # ()
print(data[:-3])  # ("a", "b", "c", "d", "e", "f", "g")
print(data[0:-6])  # ("a", "b", "c", "d")
print(data[-7:])  # ("d", "e", "f", "g", "h", "i", "j")
print(data[-7:-3])  # ("d", "e", "f", "g")
print(data[-2:-6])  # ()
print(data[3:-4])  # ("d", "e", "f")
print(data[-8:7])  # ("c", "d", "e", "f", "g")

print(data[2: 9: 2])  # ("c", "e", "g", "i")


del data  # it deletes the tuple object
