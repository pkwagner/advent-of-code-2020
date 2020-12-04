# Part I
import re

BLOCK_PATTERN = re.compile("(?:\t*\n){2}")
ENTRY_PATTERN = re.compile("(\w+):")
REQUIRED = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

with open("day4.txt", "r") as f:
  passports = [set(ENTRY_PATTERN.findall(block)) for block in BLOCK_PATTERN.split(f.read())]
  valid = list(filter(lambda p: p.issuperset(REQUIRED), passports))

  print("{} / {}".format(len(valid), len(passports)))


# Part II
import re

BLOCK_PATTERN = re.compile("(?:\t*\n){2}")
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
  passports = [{k: v for k, v in ENTRY_PATTERN.findall(block)} for block in BLOCK_PATTERN.split(f.read())]

  valid = 0
  for p in passports:
    valid += all(map(lambda x: x[0] in p and x[1].match(p[x[0]]), REQUIRED.items()))

  print("{} / {}".format(valid, len(passports)))
