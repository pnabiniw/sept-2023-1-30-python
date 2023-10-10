# While loops are used with truthy or falsy statement
# The iteration continues till the statement is truthy and breaks immediately on
# getting falsy statement

a = 0
while a < 10:
    print(a)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    a += 1
else:
    print("While loop is iterated completely")

a = 3
count = 0
while a:
    print("Hello")
    count += 1
    if count == a:
        a = 0

while True:  # this is infinite loop
    print("Hello")
