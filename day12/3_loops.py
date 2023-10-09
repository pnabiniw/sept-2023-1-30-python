# Loops are used to repeatedly execute certain blocks of code
# They help in reduce the manual effort and automate the task
# There are two types if loops in python

# 1. for loop
# 2. while loop

#  for loop takes iterable and iterates until the iterable is completely traversed
# list, tuples, set, dictionary etc. are iterables

for i in ["a", "e", "i", "o", "u"]:
    print(i)


# But the while loop takes truthy or Falsy statement and iterate until the condition is truthy

a = 0
while a < 10:
    print(a)
    a += 1

