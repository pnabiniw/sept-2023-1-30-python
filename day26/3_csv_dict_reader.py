import csv

filename = "students.csv"
result = []
with open(filename, "r") as cr:
    csv_reader = csv.DictReader(cr)
    for each in csv_reader:
        print(each)
        result.append(each)
print(result)
