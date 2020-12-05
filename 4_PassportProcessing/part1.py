import re

BLOCK_PATTERN = re.compile("(?:\t*\n){2}")
ENTRY_PATTERN = re.compile("(\w+):")
REQUIRED = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

with open("day4.txt", "r") as f:
  passports = [set(ENTRY_PATTERN.findall(block)) for block in BLOCK_PATTERN.split(f.read())]
  valid = [pp for pp in passports if pp.issuperset(REQUIRED)]

  print("{} / {}".format(len(valid), len(passports)))
