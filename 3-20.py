def f(arr):
  even = list(filter(lambda a: a % 2 == 0, arr))
  odd = list(filter(lambda a: a % 2 != 0, arr))
  return even + odd

def main():
  tests = [
    [7,9,2,4,5,6]
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')

if __name__ == "__main__":
  main()
