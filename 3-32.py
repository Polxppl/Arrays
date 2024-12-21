arr = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
]

print('Before: ', arr)

swap = arr[0]
arr[0] = arr[-1]
arr[-1] = swap

print('After: ', arr)
