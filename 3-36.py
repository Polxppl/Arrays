
def f(arr):
  return [v for xs in arr for v in xs]

def main():
  tests = [
    [
      [2,3],
      [1,5],
    ],
    [
      [5,0,3,7,5],
      [9,0,9,1,2],
    ],
    [
      [2,1],
      [3,5],
      [7,4],
      [2,6],
    ],
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')

if __name__ == "__main__":
  main()




