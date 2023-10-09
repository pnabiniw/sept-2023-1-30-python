# input a number : 15
# divide by 3 : Fizz
# divide by 5 : Buzz
# divide by both 3 and 5: FizzBuzz
# print the number itself

num = int(input("Enter a number"))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
