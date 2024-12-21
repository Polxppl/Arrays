def weekday(n):
  weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  return weekdays[n - 1]

def main():
  tests = [
    1, 4, 7
  ]
  for test in tests:
    print(f'weekday({test}) returns {weekday(test)}')



if __name__ == "__main__":
  main()
