def f(arr):
  rows = len(arr[0])
  columns = len(arr)
  result = [list(range(0, columns)) for row in range(0, rows)]
  for row in range(0, rows):
    for column in range(0, columns):
      result[row][column] = arr[column][row]
  return result

def main():
  tests = [
    [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3,4,5], [6,7,8,9,0]], [[5,6,7,8]]
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')

if __name__ == "__main__":
  main()




