arr = [[-38, 19], [5,40],[-7,11],[29,16]]

flat = [xs for x in arr for xs in x]

min = min(flat)
max = max(flat)

def find(value):
  for row in range(0, len(arr)):
    for columnm in range(0, len(arr[row])):
      if value == arr[row][columnm]:
        return [row, columnm]

print(f'Min: {min}, [x, y]: {find(min)}')
print(f'Max: {max}, [x, y]: {find(max)}')
