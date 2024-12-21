def f(a, b):
  for i in a:
    if i not in b:
      return False
  return True

def main():
  tests = [
    ([9,2,4], [7,9,2,4,5,6]), ([1,2,4], [7,9,2,4,5,6])
  ]
  for test in tests:
    print(f'f({test}) returns {f(*test)}')

if __name__ == "__main__":
  main()
