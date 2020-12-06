from functools import reduce

with open("day6.txt", "r") as f:
  group_occurrences = map(
      lambda block: len(reduce(
          lambda a, b: a & b, 
          map(lambda line: {c for c in line if c.isalnum()}, block.split("\n"))
      )), 
      f.read().split("\n\n")
  )

  print(sum(group_occurrences))
