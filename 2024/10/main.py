grid = open("./input.txt").read().splitlines()
# grid = open("./test.txt").read().splitlines()

starting_points = []
for j in range(len(grid)):
    for i in range(len(grid[j])):
        if grid[j][i] == "0":
            starting_points.append((i, j))

total_points = 0
for i, j in starting_points:
    current_point = 0
    q = [((i, j), 1)]
    visited = []
    while len(q) > 0:
        (x, y), n = q.pop(0)
        # comment this part out for this for q2
        # if (x, y) in visited:
        #     continue
        # visited.append((x, y))
        if n == 10 and int(grid[y][x]) == 9:
            print("POINT!", x, y)
            current_point += 1
            continue
        if y + 1 < len(grid) and int(grid[y + 1][x]) == n:
            q.append(((x, y + 1), n + 1))
        if y - 1 >= 0 and int(grid[y - 1][x]) == n:
            q.append(((x, y - 1), n + 1))
        if x + 1 < len(grid[0]) and int(grid[y][x + 1]) == n:
            q.append(((x + 1, y), n + 1))
        if x - 1 >= 0 and int(grid[y][x - 1]) == n:
            q.append(((x - 1, y), n + 1))

    total_points += current_point
    print(current_point)
    print("---")


print(total_points)
