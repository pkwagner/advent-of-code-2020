import re

RULE_PATTERN = re.compile("^(\w+ \w+) bags contain ([\w ,]+)\.$", re.MULTILINE)
RULE_EMISSIONS_PATTERN = re.compile("\d+ (\w+ \w+) bags?")

def outer_colors(rules, color):
  queue = set(rules[color])
  colors = set(rules[color])

  while len(queue) > 0:
    succ = queue.pop()
    if succ in rules:
      queue |= rules[succ] - colors
      colors |= rules[succ]

  return colors

with open("day7.txt", "r") as f:
  rules = {}
  for outer_color, emissions in RULE_PATTERN.findall(f.read()):
    for inner_color in RULE_EMISSIONS_PATTERN.findall(emissions):
      rules[inner_color] = rules[inner_color] | {outer_color} if inner_color in rules else {outer_color}

  print(len(outer_colors(rules, "shiny gold")))
