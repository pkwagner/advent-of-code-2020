import re

ENTRY_PATTERN = re.compile("(\w+):([^\s]+)")
REQUIRED = {
    "byr": re.compile("19[2-9]\d$|200[012]$"),
    "iyr": re.compile("201\d$|2020$"),
    "eyr": re.compile("202\d$|2030$"),
    "hgt": re.compile("1(?:[5-8]\d|9[0-3])cm$|(?:59|6\d|7[0-6])in$"),
    "hcl": re.compile("#[0-9a-f]{6}$"),
    "ecl": re.compile("(?:amb|blu|brn|gry|grn|hzl|oth)$"),
    "pid": re.compile("\d{9}$")
}

with open("day4.txt", "r") as f:
  passports = [{k: v for k, v in ENTRY_PATTERN.findall(block)} for block in f.read().split("\n\n")]

  valid = 0
  for pp in passports:
    valid += all(map(lambda x: x[0] in pp and x[1].match(pp[x[0]]), REQUIRED.items()))

  print("{} / {}".format(valid, len(passports)))
