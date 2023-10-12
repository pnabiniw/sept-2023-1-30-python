# lambda is the anonymous function in python
# They are the nameless function which is used to create a single statement function
# They are usually used in a higher order functions as a parameter

func = lambda x: print(x)
func("Hello World")

summ = lambda x, y: x + y
print(summ(2, 3))


# map()
result = map(lambda element: element ** 2, [5, 6, 7, 8])
print(list(result))  # [25, 36, 49, 64]


# filter
result = filter(lambda element: element % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(result))  # [2, 4, 6, 8]


# reduce()
from functools import reduce
nums = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, nums)
print(result)  # 15
