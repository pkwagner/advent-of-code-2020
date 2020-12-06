import re

BLOCK_PATTERN = re.compile("(?:\t*\n){2}")

with open("day6.txt", "r") as f:
  group_occurrences = map(
      lambda block: len({c for c in block if c.isalnum()}),
      BLOCK_PATTERN.split(f.read())
  )

  print(sum(group_occurrences))
