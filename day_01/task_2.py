dial = 100
moves: list[int] = []

with open("input.txt") as file:
    for line in file:
        move = line.strip()
        direction, steps = move[0], int(move[1:])
        moves.append(steps if direction == "R" else -steps)


position: int = 50
zeros: int = 0

for r in moves:
    position = (position + r) % dial
    zeros += int(position == 0)
    zeros += r > 0 and position != 0 and position < (r % dial)
    zeros += r < 0 and position > dial - (abs(r) % dial)
    zeros += abs(r) // dial

print(f"{zeros}")
