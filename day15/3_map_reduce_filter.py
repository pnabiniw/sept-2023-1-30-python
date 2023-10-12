# map(), reduce() and filter() are the built-in python functions which work with iterables
# These are also called as higher order functions (they take function as an argument)


# map(func, iterable) => map() function takes function as a first parameter and iterable as a second parameter
# It maps each element of the iterable to new form
# Count of elements in the initial iterable and final result is same


def raise_power(element):
    return element ** 2


result = map(raise_power, [5, 6, 7, 8])
print(list(result))  # [25, 36, 49, 64]

# filter(func, iterable) => filter() function also takes function as a first parameter and iterable
# as a second parameter
# It filters certain element from the iterable
# Count of elements in the initial iterable and final result may not be same

nums = [1, 2, 3, 4, 5, 6, 7, 8]


def is_even(element):
    return element % 2 == 0


result = filter(is_even, nums)
print(list(result))  # [2, 4, 6, 8]


# reduce(func, iterable) => reduce() function also takes function as a first parameter and iterable
# as a second parameter
# It reduces the iterable to single value

from functools import reduce
nums = [1, 2, 3, 4, 5]


def sum_elements(x, y):
    return x + y


result = reduce(sum_elements, nums)
print(result)  # 15
