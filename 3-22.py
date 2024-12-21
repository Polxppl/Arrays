import random
arr = [97, -3, 10, 3, -38, -97, -83, -27, -42, 88, 43, -38, 88, 31, -20, 34, 79, 68, 99, 46]

def rand_elem(v):
  return v[random.randint(0, len(arr) - 1)]

print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))
