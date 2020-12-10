with open("day6.txt", "r") as f:
  group_occurrences = map(
      lambda block: len({c for c in block if c.isalnum()}),
      f.read().split("\n\n")
  )

  print(sum(group_occurrences))
