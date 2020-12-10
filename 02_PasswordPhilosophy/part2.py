import re

PATTERN = re.compile("(\d+)-(\d+) (\w): (\w+)")

with open("day2.txt", "r") as f:
  a = PATTERN.findall(f.read())

  valid = 0
  for min, max, char, string in a:
    if (string[int(min) - 1] is char) ^ (string[int(max) - 1] is char):
      valid += 1

  print("{} / {}".format(valid, len(a)))
