import re
from collections import namedtuple
from functools import reduce
from itertools import repeat

# Directions: N -> 0, E -> 1, S -> 2, W -> 3
State = namedtuple("State", "x y wpx wpy")
Command = namedtuple("Command", "cmd arg")

CMD_PATTERN = re.compile("^(N|S|E|W|L|R|F)(\d+)$", re.MULTILINE)
TRANSITIONS = {
    "N": lambda s, v: State(s.x, s.y, s.wpx, s.wpy + v),
    "S": lambda s, v: State(s.x, s.y, s.wpx, s.wpy - v),
    "E": lambda s, v: State(s.x, s.y, s.wpx + v, s.wpy),
    "W": lambda s, v: State(s.x, s.y, s.wpx - v, s.wpy),
    "L": lambda s, v: reduce(lambda si, _: State(si.x, si.y, -si.wpy, si.wpx), repeat(None, v // 90), s),
    "R": lambda s, v: reduce(lambda si, _: State(si.x, si.y, si.wpy, -si.wpx), repeat(None, v // 90), s),
    "F": lambda s, v: State(s.x + v * s.wpx, s.y + v * s.wpy, s.wpx, s.wpy)
}

with open("day12.txt", "r") as f:
  commands = [Command(cmd, int(arg)) for cmd, arg in CMD_PATTERN.findall(f.read())]

  initial_state = State(0, 0, 10, 1)
  final_state = reduce(lambda state, cmd: TRANSITIONS[cmd.cmd](state, cmd.arg), commands, initial_state)

  print(abs(final_state.x) + abs(final_state.y))
