def identity_matrix(n):
  return [[int((row * n + column) % (n + 1) == 0) for column in range(0, n)] for row in range(0, n)]

def print_matrix(arr):
  result = '\n'.join([' '.join(str(cell) for cell in row) for row in arr])
  print(result)

matrix3 = identity_matrix(3)
matrix5 = identity_matrix(5)
matrix8 = identity_matrix(8)

print_matrix(matrix3)
print_matrix(matrix5)
print_matrix(matrix8)
