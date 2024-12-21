def f(a, b):
  if len(a) != len(b):
    return False
  for i in range(0, len(a)):
    if a[i] != b[i]:
      return False
  return True

def main():
  tests = [
    (["water","book","sky"], ["water","book","sky"]),
    ([True,False], [True,False,True]),
    ([5,3,1], [5,3,1]),
    ([3,2,1], [3,2])
  ]
  for test in tests:
    print(f'f({test}) returns {f(*test)}')



if __name__ == "__main__":
  main()
