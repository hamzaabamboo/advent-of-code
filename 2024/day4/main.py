f = open("./input.txt")

g = f.readlines()

q1 = 0
for j in range(0, len(g)):
    for i in range(0, len(g[j])):
        if g[j][i] == "X":
            right = i + 3 < len(g[j])
            left = i - 3 >= 0
            down = j + 3 < len(g)
            up = j - 3 >= 0
            conditions = [
                right and g[j][i + 1] + g[j][i + 2] + g[j][i + 3] == "MAS",
                left and g[j][i - 1] + g[j][i - 2] + g[j][i - 3] == "MAS",
                down and g[j + 1][i] + g[j + 2][i] + g[j + 3][i] == "MAS",
                up and g[j - 1][i] + g[j - 2][i] + g[j - 3][i] == "MAS",
                right
                and down
                and g[j + 1][i + 1] + g[j + 2][i + 2] + g[j + 3][i + 3] == "MAS",
                left
                and down
                and g[j + 1][i - 1] + g[j + 2][i - 2] + g[j + 3][i - 3] == "MAS",
                right
                and up
                and g[j - 1][i + 1] + g[j - 2][i + 2] + g[j - 3][i + 3] == "MAS",
                left
                and up
                and g[j - 1][i - 1] + g[j - 2][i - 2] + g[j - 3][i - 3] == "MAS",
            ]
            q1 += sum([1 if c else 0 for c in conditions])

q2 = 0
for j in range(1, len(g) - 1):
    for i in range(1, len(g[j]) - 1):
        if g[j][i] == "A":
            is_xmas = (
                (g[j - 1][i - 1] == "M" and g[j + 1][i + 1] == "S")
                or (g[j - 1][i - 1] == "S" and g[j + 1][i + 1] == "M")
            ) and (
                (g[j + 1][i - 1] == "M" and g[j - 1][i + 1] == "S")
                or (g[j + 1][i - 1] == "S" and g[j - 1][i + 1] == "M")
            )

            if is_xmas:
                q2 += 1
print(q1)
print(q2)
