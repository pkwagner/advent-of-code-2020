# Part I
DIRECTION = (1, 3)

with open("day3.txt", "r") as f:
  map = [[x == "#" for x in row.rstrip()] for row in f.readlines()]
  
  pos, trees = (0, 0), 0
  while True:
    pos = x, y = pos[0] + DIRECTION[0], (pos[1] + DIRECTION[1]) % len(map[0])

    if x >= len(map):
      break

    trees += map[x][y]

  print(trees)


# Part II
DIRECTIONS = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

with open("day3.txt", "r") as f:
  map = [[x == "#" for x in row.rstrip()] for row in f.readlines()]
  
  result = 1
  for d in DIRECTIONS:
    pos, trees = (0, 0), 0
    while True:
      pos = x, y = pos[0] + d[0], (pos[1] + d[1]) % len(map[0])

      if x >= len(map):
        break

      trees += map[x][y]

    result *= trees

  print(result)
