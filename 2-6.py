matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i in range(0, len(matrix)):
  for j in range(0, len(matrix[i])):
    if (j + i * len(matrix[i])) % 4 == 0:
      matrix[i][j] = 1

print(matrix)
