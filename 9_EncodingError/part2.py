TARGET = 15690279

with open("day9.txt", "r") as f:
  nmbrs = [int(x) for x in f.readlines()]
  
  for i in range(len(nmbrs)):
    nmbr = nmbrs[i]
    min_nmbr, max_nmbr, sum = nmbr, nmbr, nmbr
    for second_nmbr in nmbrs[i + 1:]:
      min_nmbr, max_nmbr = min(min_nmbr, second_nmbr), max(max_nmbr, second_nmbr)
      sum += second_nmbr

      if sum == TARGET:
        print(min_nmbr + max_nmbr)
      elif sum > TARGET:
        break
