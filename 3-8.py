arr = [2, 6, 4, 9, 7]

def star(n):
  return ''.join(['*' for _ in range(0, n)])

for i in arr:
  print(f'{i}: {star(i)}')
