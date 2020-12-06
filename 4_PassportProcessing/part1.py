import re

ENTRY_PATTERN = re.compile("(\w+):")
REQUIRED = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

with open("day4.txt", "r") as f:
  passports = [set(ENTRY_PATTERN.findall(block)) for block in f.read().split("\n\n")]
  valid = [pp for pp in passports if pp.issuperset(REQUIRED)]

  print("{} / {}".format(len(valid), len(passports)))
