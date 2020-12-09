PREAMBLE_LENGTH = 25

with open("day9.txt", "r") as f:
  nmbrs = [int(x) for x in f.readlines()]
  sums = {}
  
  # Calculate sums for preamble
  for i in range(1, PREAMBLE_LENGTH):
    nmbr = nmbrs[i - 1]
    for sum in map(lambda x: x + nmbr, nmbrs[i : PREAMBLE_LENGTH]):
      sums[sum] = sums[sum] + 1 if sum in sums else 1

  for i in range(PREAMBLE_LENGTH, len(nmbrs) - 1):
    current_nmbr = nmbrs[i]
    if current_nmbr not in sums or sums[current_nmbr] <= 0:
      print(current_nmbr)
      break

    # Add new sum and remove outdated ones
    outdated_nmbr = nmbrs[i - PREAMBLE_LENGTH]
    for nmbr in nmbrs[i - PREAMBLE_LENGTH + 1 : i]:
      new_sum = nmbr + current_nmbr
      sums[new_sum] = sums[new_sum] + 1 if new_sum in sums else 1

      outdated_sum = nmbr + outdated_nmbr
      sums[outdated_sum] -= 1
