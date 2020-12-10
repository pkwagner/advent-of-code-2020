with open("day10.txt", "r") as f:
  joltages = sorted([int(x) for x in f.readlines()])
  joltages = [0] + joltages + [joltages[-1] + 3]

  gaps = {}
  for prev, curr in zip(joltages, joltages[1:]):
    gap = curr - prev
    gaps[gap] = gaps[gap] + 1 if gap in gaps else 1

  print(gaps.get(1, 0) * gaps.get(3, 0))
