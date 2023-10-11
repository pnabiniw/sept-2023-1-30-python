# break, continue and pass are the control statements in Python

# 1. break => It breaks the loop without complete iteration
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

num = 0
while num < 10:
    if num == 5:
        break
    print(num)
    num += 1


# 2. continue => It skips a step and continues the loop
for i in range(10):
    if i == 5:
        continue
    print(i)   # 0, 1, 2, 3, 4, 6, 7, 8, 9


num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1

# 3. pass => It is used as a placeholder for the codes in the future. It is used to make the code
# syntactically correct, but it doesn't do anything


def addition():
    pass
