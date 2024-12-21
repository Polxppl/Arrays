arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

result = filter(lambda a: a not in arr2, arr1)
print(list(result))
