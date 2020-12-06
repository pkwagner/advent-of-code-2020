import re
from functools import reduce

BLOCK_PATTERN = re.compile("(?:\t*\n){2}")

with open("day6.txt", "r") as f:
  group_occurrences = map(
      lambda block: len(reduce(
          lambda a, b: a & b, 
          map(lambda line: {c for c in line if c.isalnum()}, block.split("\n"))
      )), 
      BLOCK_PATTERN.split(f.read())
  )

  print(sum(group_occurrences))
