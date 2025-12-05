nodes = set()

with open("input.txt", "r") as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            if char == "@":
                nodes.add((x, y))


def count_adjecent_rolls(nodes: set[tuple[int, int]]) -> int:
    accessible = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for node in nodes:
        count = 0
        for dx, dy in directions:
            neighbor = (node[0] + dx, node[1] + dy)
            if neighbor in nodes:
                count += 1

        if count < 4:
            accessible.add(node)

    return len(accessible)


result = count_adjecent_rolls(nodes)
print(result)
