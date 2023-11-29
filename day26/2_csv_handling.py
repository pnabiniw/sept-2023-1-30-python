# CSV stands for Comma Separated Values
# CSV files have extension .csv
import csv

filename = "students.csv"
with open(filename, "r") as cr:
    result = []
    for count, eachline in enumerate(csv.reader(cr)):
        if count == 0:
            continue
        student = {"name": eachline[0], "email": eachline[1],
                   "age": eachline[2], "address": eachline[3]}
        result.append(student)
print(result)

# result = [
#     {"name": "Jon", "age": 30, "email": "j@email.com", "address": "KTM"},
#     {"name": "Jon", "age": 30, "email": "j@email.com", "address": "KTM"},
#     {"name": "Jon", "age": 30, "email": "j@email.com", "address": "KTM"},
# ]
