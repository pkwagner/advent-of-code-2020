import re

RULE_PATTERN = re.compile("^(\w+ \w+) bags contain ([\w ,]+)\.$", re.MULTILINE)
RULE_EMISSIONS_PATTERN = re.compile("(\d+) (\w+ \w+) bags?")

# Return includes outermost bag itself!
def inner_bag_count(rules, color, known={}):
  cnt = 1
  for count, subcolor in rules[color]:
    if subcolor not in known:
      known[subcolor] = inner_bag_count(rules, subcolor, known)
    
    cnt += count * known[subcolor]

  return cnt


with open("day7.txt", "r") as f:
  rules = {color: {(int(count), subcolor) for count, subcolor in RULE_EMISSIONS_PATTERN.findall(sub)} for color, sub in RULE_PATTERN.findall(f.read())}

  print(inner_bag_count(rules, "shiny gold") - 1)
