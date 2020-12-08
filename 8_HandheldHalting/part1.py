import re

CMD_PATTERN = re.compile("^(acc|jmp|nop) ([+-]\d+)$", re.MULTILINE)

with open("day8.txt", "r") as f:
  program = [(cmd, int(arg)) for cmd, arg in CMD_PATTERN.findall(f.read())]

  state, counter = 0, 0
  while program[counter] != None:
    cmd, arg = program[counter]
    program[counter] = None

    if cmd == "acc":
      state += arg
      counter += 1
    elif cmd == "jmp":
      counter += arg
    elif cmd == "nop":
      counter += 1

  print(state)
