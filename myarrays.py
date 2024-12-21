def bubble_sort(arr):
  n = len(arr)
  for i in range(0, n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j+1]:
        swap = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = swap
  return arr

def second_largest(arr):
  (first, second) = (arr[0], arr[0])
  for i in arr:
    if i > first:
      second = first
      first = i
  return second

def min_max_diff(arr):
  (min, max) = (arr[0], arr[0])
  for i in arr:
    if i > max:
      max = i
    if i < min:
      min = i
  return max - min

def min_max(arr):
  (min, max) = (arr[0], arr[0])
  for i in arr:
    if i > max:
      max = i
    if i < min:
      min = i
  return [min, max]

def median(arr):
  sorted = bubble_sort(arr)
  if len(arr) % 2 == 0:
    return (sorted[len(arr) / 2] + sorted[len(arr) / 2 + 1]) / 2
  else:
    return sorted[int(len(arr) / 2) + 1]

def stringify(arr):
  return '-'.join([str(a) for a in arr])

