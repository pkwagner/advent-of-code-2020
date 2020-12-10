MAXGAP = 3

with open("day10.txt", "r") as f:
  joltages = sorted([int(x) for x in f.readlines()])
  joltages = [0] + joltages + [joltages[-1] + 3]

  # Intuition: Calculate solution count of each joltage based on the prior partial solutions (initially: 1)
  # Nested loop is limited to MAXGAP iterations because of strict joltage ordering, hence complexity is still O(n)
  solutions = [1] + [0] * (len(joltages) - 1)
  for i in range(1, len(joltages)):
    for j in range(i - 1, -1, -1):
      if joltages[i] - joltages[j] > MAXGAP:
        break

      solutions[i] += solutions[j]

  print(solutions[-1])
