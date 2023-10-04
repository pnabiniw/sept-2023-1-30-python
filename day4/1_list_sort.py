# sort(key:optional, reverse:optional)
a = [4, 5, 1, 3, 10, 6, 9, 2, 7]
r = a.sort()
print(r)  # None
print(a)  # [1, 2, 3, 4, 5, 6, 7, 9, 10]

a.sort(reverse=True)
print(a)  # [10, 9, 7, 6, 5, 4, 3, 2, 1]


a = [(5, 2), (6, 5), (4, 1), (8, 10), (12, 3)]
# [(4, 1), (5, 2), (12, 3), (6, 5), (8, 10)]

def get_second_element(data):
    return data[1]  # 2, 5, 1, 10, 3  (1, 2, 3, 5, 10)

a.sort(key=get_second_element)
print(a)  # [(4, 1), (5, 2), (12, 3), (6, 5), (8, 10)]


a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]
def get_last_item(data):
    return data[-1]

a.sort(key=get_last_item)
print(a)  # [(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]


