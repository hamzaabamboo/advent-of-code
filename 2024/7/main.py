grid = open("./input.txt").read().splitlines()
# grid = open("./test.txt").read().splitlines()

commands = []

for line in grid:
    result, operators = line.split(":")
    commands.append((int(result), [int(o) for o in operators.strip().split(" ")]))


def check_valid_command(command):
    return _check_valid_command((command[0], command[1][1:]), command[1][0])


def _check_valid_command(command, acc):
    total, remaining = command
    if acc > total:
        return False
    if len(remaining) == 0:
        return total == acc
    current = remaining[0]
    return (
        _check_valid_command((total, remaining[1:]), acc + current)
        or _check_valid_command((total, remaining[1:]), acc * current)
        or _check_valid_command((total, remaining[1:]), int(str(acc) + str(current)))
    )


ans = 0

for command in commands:
    if check_valid_command(command):
        ans += command[0]

print(ans)
