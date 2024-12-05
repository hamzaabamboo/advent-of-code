import math
input = open('./input.txt').read()
smolgrid =[ [ int(n) for n in row ] for row in input.split("\n")]
oM = len(smolgrid)
oN = len(smolgrid[0])
sumGrid = [
  [0, 1, 2, 3, 4],
  [1, 2, 3, 4, 5],
  [2, 3, 4, 5, 6],
  [3, 4, 5, 6, 7],
  [4, 5, 6, 7, 8]
]
grid =[ [ (((smolgrid[row %oN][column % oM] + sumGrid[math.floor(row/oM)][math.floor(column/oN)]) - 1) % 9) + 1 for column in range(oN * 5)] for row in range(oM*5)]
m = len(grid)
n = len(grid[0])
dp = [ [-1 for _ in range(n)] for _ in range(m)]
dp[0][0] = 0
print(len(smolgrid), len(grid), len(dp))
for step in range(10):
  for y in range(m):
    for x in range(n):
      if (y,x) == (0,0): continue
      candidates = [dp[y-1][x] if y > 0 else None, dp[y][x-1] if x > 0 else None, dp[y+1][x] if y < m - 1 else None , dp[y][x+1] if x < n - 1 else None ]
      dp[y][x] = min([c for c in candidates if c!= -1 and  c != None]) + grid[y][x]
print(dp[-1][-1])