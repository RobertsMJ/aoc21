from dataclasses import dataclass


@dataclass
class Position:
    horizontal: int = 0
    depth: int = 0


pos = Position()
with open("in.txt", "r") as f:
    input = f.read().splitlines()
    for cmd in input:
        cmd = cmd.split()
        direction = cmd[0]
        distance = int(cmd[1])
        if direction == "down":
            pos.depth += distance
        elif direction == "up":
            pos.depth -= distance
        elif direction == "forward":
            pos.horizontal += distance

print(pos.depth * pos.horizontal, pos.depth, pos.horizontal)
