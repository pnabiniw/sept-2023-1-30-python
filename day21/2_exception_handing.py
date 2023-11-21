# Exceptions in python are handled using try....except block

# try block should contain the error-prone code

try:
    a = int(input("Enter a number"))
except:
    print("Enter a valid number")

# There are multiple formats in which we can write try...except block
# 1. Simple try...except
# 2. try...except with proper error name mentioned in except block
# 3. Multiple error names in the same except block.
# 4. Multiple except blocks
# 5. try...except...else block
# 6. try...except...else...finally block

# 2. try...except with proper error name mentioned in except block
try:
    a = int(input("Enter a number"))
except ValueError:
    print("Enter a valid number")


# 3. Multiple error names in the same except block.
try:
    a = int(input("Enter a number"))
except (ValueError, IndexError, ZeroDivisionError):
    print("Enter a valid number")

# 4. Multiple except blocks
try:
    a = int(input("Enter a number"))
except ValueError:
    print("Enter a valid number")
except IndexError:
    print("Provide proper indexing")
except ZeroDivisionError:
    print("Denominator should not contain zero")


# try block is executed everytime. If error occurs then, except block is executed. If no
# error else block is executed. finally block is executed everytime.
# 5. try...except...else block

try:
    a = int(input("Enter a number"))
    b = int(input("Enter another number"))
except:
    print("Enter valid number")
else:
    summ = a + b
    diff = a - b
    mul = a * b
    print(summ)
    print(diff)
    print(mul)
finally:
    print("It is executed")

fp = open("jfnds.txt", "r")
try:
    a = 1
    b = 2
    print(a + b)
finally:
    fp.close()
