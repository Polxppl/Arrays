def bubble_sort(arr):
  n = len(arr)
  for i in range(0, n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j+1]:
        swap = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = swap
  return arr

def main():
  tests = [
    [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3], [-150, -20, 300, -45, -60, 500, -120]
  ]
  for test in tests:
    print(f'bubble_sort({test}) returns {bubble_sort(test)}')



if __name__ == "__main__":
  main()
