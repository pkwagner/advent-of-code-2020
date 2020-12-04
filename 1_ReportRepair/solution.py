# Part I
with open("day1.txt", "r") as f:
  nmbrs = [int(x) for x in f.readlines()]

  for i in range(len(nmbrs)):
    for j in range(i + 1, len(nmbrs)):
      if nmbrs[i] + nmbrs[j] == 2020:
        print(nmbrs[i] * nmbrs[j])


# Part II
with open("day1.txt", "r") as f:
  nmbrs = [int(x) for x in f.readlines()]

  for i in range(len(nmbrs)):
    for j in range(i + 1, len(nmbrs)):
      for k in range(j + 1, len(nmbrs)):
        if nmbrs[i] + nmbrs[j] + nmbrs[k] == 2020:
          print(nmbrs[i] * nmbrs[j] * nmbrs[k])
