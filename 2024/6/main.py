grid = open("./input.txt").read().split()
# grid = open("./test.txt").read().split()

w, h = len(grid[0]), len(grid)
obstacles = [[False for _ in range(w)] for _ in range(h)]
visited = []
starting_position = None

print(w, h)
for j in range(h):
    for i in range(w):
        if grid[j][i] == "^":
            starting_position = (i, j)
        elif grid[j][i] == "#":
            obstacles[j][i] = grid

visited = [[[] for _ in range(w)] for _ in range(h)]


def print_board():
    for j in range(h):
        line = ""
        for i in range(w):
            if obstacles[j][i]:
                line += "#"
            elif visited[j][i]:
                line += "X"
            else:
                line += "."
        print(line)


def in_bounds(p: (int, int)):
    return p[0] >= 0 and p[0] < w and p[1] >= 0 and p[1] < h


def get_next_block(position, direction):
    i, j = position
    if direction == 0:
        next_block = (i, j - 1)
    elif direction == 1:
        next_block = (i + 1, j)
    elif direction == 2:
        next_block = (i, j + 1)
    elif direction == 3:
        next_block = (i - 1, j)
    return next_block


position = starting_position
direction = 0

while in_bounds(position):
    i, j = position
    if not (position, direction) in visited[j][i]:
        visited[j][i].append((position, direction))
    next_block = get_next_block(position, direction)
    if in_bounds(next_block) and obstacles[next_block[1]][next_block[0]]:
        direction = (direction + 1) % 4
    else:
        position = next_block

print(f"final position: {position}")
print(sum([sum([len(c) > 0 for c in r]) for r in visited]))


def has_loop(obstacle):
    position = starting_position
    direction = 0

    visited = [[[] for _ in range(w)] for _ in range(h)]

    while in_bounds(position):
        i, j = position
        pos_obstacle = (position, direction)
        if pos_obstacle in visited[j][i]:
            return True
        else:
            visited[j][i].append((position, direction))

        next_block = get_next_block(position, direction)

        if in_bounds(next_block) and (
            obstacles[next_block[1]][next_block[0]] or next_block == obstacle
        ):
            direction = (direction + 1) % 4
        else:
            position = next_block
    return False


loop_count = 0

for j in range(h):
    for i in range(w):
        if obstacles[j][i]:
            continue
        if has_loop((i, j)):
            loop_count += 1

print(loop_count)
# print_board()
