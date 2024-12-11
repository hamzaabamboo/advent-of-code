from itertools import combinations

grid = open("./input.txt").read().splitlines()
# grid = open("./test.txt").read().splitlines()

nodes = {}

for j in range(len(grid)):
    for i in range(len(grid[j])):
        if grid[j][i] == ".":
            continue
        if not grid[j][i] in nodes:
            nodes[grid[j][i]] = []
        nodes[grid[j][i]].append((i, j))

antinodes = [[False for _ in range(len(grid[j]))] for j in range(len(grid))]

pairs = sum([list(combinations(nodes[k], 2)) for k in nodes], [])


def print_board():
    for j in range(len(grid)):
        row = ""
        for i in range(len(grid[j])):
            if antinodes[j][i] and grid[j][i] == ".":
                row += "#"
            else:
                row += grid[j][i]
        print(row)


print_board()

# q1
# for pair in pairs:
#     a, b = pair
#     dx = b[0] - a[0]
#     dy = b[1] - a[1]
#     p1 = (b[0] + dx, b[1] + dy)
#     p2 = (a[0] - dx, a[1] - dy)
#     print(a, b, dx, dy, p1, p2)
#     if (
#         p1[0] >= 0
#         and p1[1] >= 0
#         and p1[0] < len(antinodes[0])
#         and p1[1] < len(antinodes)
#     ):
#         antinodes[p1[1]][p1[0]] = True
#     if (
#         p2[0] >= 0
#         and p2[1] >= 0
#         and p2[0] < len(antinodes[0])
#         and p2[1] < len(antinodes)
#     ):
#         antinodes[p2[1]][p2[0]] = True

# 2
for pair in pairs:
    a, b = pair
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    antinodes[a[1]][a[0]] = True
    antinodes[b[1]][b[0]] = True
    p1 = (b[0] + dx, b[1] + dy)
    while (
        p1[0] >= 0
        and p1[1] >= 0
        and p1[0] < len(antinodes[0])
        and p1[1] < len(antinodes)
    ):
        antinodes[p1[1]][p1[0]] = True
        p1 = (p1[0] + dx, p1[1] + dy)
    p2 = (a[0] - dx, a[1] - dy)
    while (
        p2[0] >= 0
        and p2[1] >= 0
        and p2[0] < len(antinodes[0])
        and p2[1] < len(antinodes)
    ):
        antinodes[p2[1]][p2[0]] = True
        p2 = (p2[0] - dx, p2[1] - dy)


print(sum([sum([1 if a else 0 for a in r]) for r in antinodes]))

print(print_board())
