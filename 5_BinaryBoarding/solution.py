# Part I
lower_half = lambda a, b: (a, b - (b - a + 1) // 2)
upper_half = lambda a, b: (a + (b - a + 1) // 2, b)
seat_selectors = {
    "F": lambda r, c: (lower_half(*r), c),
    "B": lambda r, c: (upper_half(*r), c),
    "L": lambda r, c: (r, lower_half(*c)),
    "R": lambda r, c: (r, upper_half(*c))
}

def seat_id(code, row=(0, 127), column=(0, 7)):
  if len(code) == 0:
    assert(row[0] == row[1])
    assert(column[0] == column[1])
    return row[0] * 8 + column[0]

  return seat_id(code[1:], *seat_selectors[code[0]](row, column))

with open("day5.txt", "r") as f:
  max_id = max(map(lambda seat: seat_id(seat.rstrip()), f.readlines()))
  print(max_id)


# Part II
from functools import reduce

lower_half = lambda a, b: (a, b - (b - a + 1) // 2)
upper_half = lambda a, b: (a + (b - a + 1) // 2, b)
seat_selectors = {
    "F": lambda r, c: (lower_half(*r), c),
    "B": lambda r, c: (upper_half(*r), c),
    "L": lambda r, c: (r, lower_half(*c)),
    "R": lambda r, c: (r, upper_half(*c))
}

def seat_id(code, row=(0, 127), column=(0, 7)):
  if len(code) == 0:
    assert(row[0] == row[1])
    assert(column[0] == column[1])
    return row[0] * 8 + column[0]

  return seat_id(code[1:], *seat_selectors[code[0]](row, column))

with open("day5.txt", "r") as f:
  seat_ids = [seat_id(seat.rstrip()) for seat in f.readlines()]
  min_seat = min(seat_ids)

  # Doing some xor magic oO
  missing = reduce(
      lambda a, b: a ^ b[0] ^ b[1], 
      enumerate(seat_ids, min_seat + 1), 
      min_seat
  )

  print(missing)
