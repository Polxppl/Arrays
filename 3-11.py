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
    [97, -3, 10, 3, -38, -97, -83, -27, -42, 88, 43, -38, 88, 31, -20, 34, 79, 68, 99, 46],
    [-64, 16, 16, 86, -46, 98, 55, -81, -34, -73, 82, 14, 8, -43, -86, -92, -42, 78, 75, 36],
    [6, -99, -71, -77, -47, 55, -15, -83, -32, -47, -27, -56, -34, -6, -87, -26, -12, 61, -18, 44]
  ]
  for test in tests:
    print(f'bubble_sort({test}) returns {bubble_sort(test)}')





if __name__ == "__main__":
  main()
