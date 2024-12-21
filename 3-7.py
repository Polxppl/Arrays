arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

longest = max(arr, key=lambda a: len(a))

print(f'Names: {arr}')
print(f'Longest name: {longest}')
