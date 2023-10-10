# For loops are applicable in iterables / sequence datatypes

vowels = ["a", "e", "i", "o", "u"]
for vowel in vowels:
    print(vowel)
else:
    print("All the items are iterated")

# for loop also supports else statement in Python. else statement is executed after the loop is completely
# iterated

# for loop in dictionary
student = {"name": "Jane", "age": 34, "address": "KTM"}
for each in student:
    print(each)  # name, age, address

for each in student.values():
    print(each)  # Jane, 34, KTM

for each in student.keys():
    print(each)  # name, age, address


for each in student.items():
    print(each)  # (name, Jane)   (age, 34)   (address, KTM)


for key, value in student.items():
    print(key)
    print(value)


# range() function
# range() is a built-in function which gives the sequence of number starting from 0

print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(4, 8)))  # [4, 5, 6, 7]
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]

for i in range(10):
    print(i)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

even_numbers = [i for i in range(20) if i % 2 == 0]  # list comprehension
print(even_numbers)


# enumerate()
# enumerate() is also a built-in function that gives the count of the loop

# for(i=0;i<=10;i++){
#     print("Hello")
# }

vowels = ["a", "e", "i", "o", "u"]
count = 0
for i in vowels:
    print(count)
    count += 1
    print(i)

result = enumerate(vowels)
print(list(result))


for count, value in enumerate(vowels):
    print(count)  # 0, 1, 2, 3, 4
    print(value)  # a, e, i, o, u


for count, value in enumerate(vowels, start=1):
    print(count)  # 1, 2, 3, 4, 5
    print(value)  # a, e, i, o, u


# Dictionary comprehension
students = [("name", "Alex"), ("age", 30), ("address", "KTM")]
students_dict = {key: value for key, value in students}
print(students_dict)  # {"name": "Alex", "age": 30, "address": "KTM"}

data = {i: i for i in range(5)}
print(data)  # {0:0, 1:1, 2:2, 3:3, 4:4}
