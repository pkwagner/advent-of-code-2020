import re
from collections import namedtuple
from functools import reduce

# Directions: N -> 0, E -> 1, S -> 2, W -> 3
State = namedtuple("State", "dir x y")
Command = namedtuple("Command", "cmd arg")

CMD_PATTERN = re.compile("^(N|S|E|W|L|R|F)(\d+)$", re.MULTILINE)
TRANSITIONS = {
    "N": lambda s, v: State(s.dir, s.x, s.y + v),
    "S": lambda s, v: State(s.dir, s.x, s.y - v),
    "E": lambda s, v: State(s.dir, s.x + v, s.y),
    "W": lambda s, v: State(s.dir, s.x - v, s.y),
    "L": lambda s, v: State((s.dir - v // 90) % 4, s.x, s.y),
    "R": lambda s, v: State((s.dir + v // 90) % 4, s.x, s.y),
    "F": lambda s, v: State(s.dir, s.x + v * ((s.dir == 1) - (s.dir == 3)), s.y + v * ((s.dir == 0) - (s.dir == 2)))
}

with open("day12.txt", "r") as f:
  commands = [Command(cmd, int(arg)) for cmd, arg in CMD_PATTERN.findall(f.read())]

  initial_state = State(1, 0, 0)
  final_state = reduce(lambda state, cmd: TRANSITIONS[cmd.cmd](state, cmd.arg), commands, initial_state)

  print(abs(final_state.x) + abs(final_state.y))
