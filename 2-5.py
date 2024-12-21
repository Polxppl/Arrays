
# calculates how many seats are available
# calculates how many seats are booked
# informs what the status of a seat is in a given row and given place (available or booked)
# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def flat(arr):
  return [x for xs in cinema_seats for x in xs]

def seats_total(seats):
  total = 0
  for row in seats:
    total += len(row)
  return total

def seats_available(seats):
  return len(list(filter(lambda v: v == 'A', flat(seats))))

def seats_booked(seats):
  return len(list(filter(lambda v: v == 'B', flat(seats))))

def seat_status(seats, row, place):
   return seats[row - 1][place - 1]

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
