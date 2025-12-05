nodes = set()

with open("input.txt", "r") as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            if char == "@":
                nodes.add((x, y))


def nodes_to_remove(nodes: set[tuple[int, int]]) -> int:
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

    return accessible


removed = 0
while to_remove := nodes_to_remove(nodes):
    nodes -= to_remove
    removed += len(to_remove)

print(removed)
