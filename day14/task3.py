"""
Create a new list of repeated items from a provided list:
nums = [3, 4, 2, 2, 1, 3, 3, 3]
Output = [3, 2]

"""
nums = [3, 4, 2, 2, 1, 3, 3, 3]
result = []
for num in nums:
    if nums.count(num) > 1 and num not in result:
        result.append(num)
print(result)


