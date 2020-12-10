import re

CMD_PATTERN = re.compile("^(acc|jmp|nop) ([+-]\d+)$", re.MULTILINE)

def evaluate(program):
  seen = [False] * len(program)

  state, counter, jn_trace = 0, 0, []
  while counter < len(program) and not seen[counter]:
    cmd, arg = program[counter]
    seen[counter] = True

    if cmd == "acc":
      state += arg
      counter += 1
    elif cmd == "jmp":
      jn_trace.append(counter)
      counter += arg
    elif cmd == "nop":
      jn_trace.append(counter)
      counter += 1

  return counter == len(program), state, jn_trace

with open("day8.txt", "r") as f:
  program = [(cmd, int(arg)) for cmd, arg in CMD_PATTERN.findall(f.read())]

  # Intuition: Track jmp / nop executions, then replace them step by step (reversed)
  _, _, trace = evaluate(program)
  for line in reversed(trace):
    original = program[line]
    program[line] = "jmp" if original[0] == "nop" else "nop", original[1]

    success, state, _ = evaluate(program)
    if success:
      print(state)
      break

    program[line] = original
