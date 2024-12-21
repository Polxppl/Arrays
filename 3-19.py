arr = [97, -3, 10, 3, -38, -97, -83, -27, -42, 88, 43, -38, 88, 31, -20, 34, 79, 68, 99, 46]

number = int(input('Number: '))

print('Count: ', len(list(filter(lambda a: a > number, arr))))
