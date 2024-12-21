# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

total_expenses = [0, 0, 0]

for i in monthly_expenses:
  for j in range(0, 3):
    total_expenses[j] += i[j]

weeks = [0, 0, 0, 0]
for i in range(0, len(monthly_expenses)):
  weeks[i] = sum(monthly_expenses[i])

month = sum(weeks)

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food: ', total_expenses[0])
print('Transport: ', total_expenses[1])
print('Utilities: ', total_expenses[2])
print('Week 1: ', weeks[0])
print('Week 2: ', weeks[1])
print('Week 3: ', weeks[2])
print('Week 4: ', weeks[3])
print('---------------')
print('TOTAL:', month)
