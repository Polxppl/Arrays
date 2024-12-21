arr = [15, 8, 31, 47, 2, 19]

i = 0
total = 0

while i < len(arr):
  total += arr[i]
  i += 1

print(f'Array: {arr}')
print(f'Arithmetic mean: {total / len(arr)}')
