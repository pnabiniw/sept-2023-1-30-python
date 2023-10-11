"""WAP to delete all the occurrences of a specified character in a given string
S = “All the occurrences of a specified character in a given string”
Input = “a”
Output = “ll occurrences of  specified chrcter in  given string”
"""

s = "All the occurrences of a specified character in a given string"
char = input("Enter a character ")  # a
result = ""
for i in s:
    if i.lower() == char.lower():  # l == a
        continue
    result += i  # "ll the occurrences of specified charcter in given string"

print(result)
