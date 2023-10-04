# Set in python are mutable datatype. However, every element of a set must be immutable
# Set doesn't support indexing and slicing
# Set elements are always unique
# Set are unordered. {1, 2} and {2, 1} are same.
# Set are created by enclosing objects in curly braces.

# Creating an empty set
a = set()
# a = {}  # This is not an empty set. It is an empty dictionary

# Creating non-empty set
data = {1, 2, 3, 4}  # Set of integers and all elements are immutable
fruits = {"apple", "mango", "banana"}  # set of strings and all elements are immutable
a = {1, "a", (1, 2), 2.2}  # set of mixed type but all elements are immutable
print(a)

# a = {[1, 2], "hello"}  # Invalid because set elements can't be mutable
# a = {(1, 2, ["hello", "World"]), 3}  # Invalid because tuple has a list element


