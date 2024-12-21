
arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for row in range(1, len(arr) + 1):
  for column in range(1, len(arr[row - 1]) + 1):
    arr[row - 1][column - 1] = row * column

print(arr)
