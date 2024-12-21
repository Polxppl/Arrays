arr = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
]

print('Before: ', arr)

for row in arr:
  swap = row[-1]
  row[-1] = row[0]
  row[0] = swap

print('After: ', arr)
