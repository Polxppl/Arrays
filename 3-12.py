
arr = [2, 3, 2, 5, 8, 1, 9, 8]
print('Array: ', arr)
unique = list(filter(lambda a: arr.count(a) == 1, arr))
print('Unique elements: ', unique)
