grid = open("./input.txt").read().split()
# grid = open("./test.txt").read().split()


def blink(dp, stone, it):
    if it == 0:
        return 1
    if stone in dp[it]:
        return dp[it][stone]
    if stone == 0:
        dp[it][stone] = blink(dp, 1, it - 1)
    elif len(str(stone)) % 2 == 0:
        halfpoint = int(len(str(stone)) / 2)
        dp[it][stone] = blink(dp, int(str(stone)[0:halfpoint]), it - 1) + blink(
            dp, int(str(stone)[halfpoint:]), it - 1
        )
    else:
        dp[it][stone] = blink(dp, stone * 2024, it - 1)
    return dp[it][stone]


N = 76
dp = [{} for n in range(N)]
stones = [int(n) for n in grid]

for it in range(N):
    print(sum([blink(dp, stone, it) for stone in stones]))

print(len(stones))
