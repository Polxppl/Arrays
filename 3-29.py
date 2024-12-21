def f(x, y):
  return [[0 for columns in range(0, y)] for row in range(0, x)]

def main():
  tests = [
    (3, 5)
  ]
  for test in tests:
    print(f'f({test}) returns {f(*test)}')

if __name__ == "__main__":
  main()
