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
