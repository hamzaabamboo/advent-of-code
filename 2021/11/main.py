input = open("./input.txt").read()
grid = [[int(n) for n in line] for line in input.split("\n")]
m = len(grid)
n = len(grid[0])

def getPossiblePos(y,x):
  pY = [y]
  pX = [x]
  if y > 0: pY.append(y-1)
  if y < m-1: pY.append(y+1)
  if x > 0: pX.append(x-1)
  if x < n-1: pX.append(x+1)
  p = []
  for y in pY:
    for x in pX:
      p.append((y,x))
  return p[1:]

def isSynced(grid):
  return all([all([n == grid[0][0] for n in row]) for row in grid])
count = 0
step = 0
while not isSynced(grid):
  step += 1
  flashed = []
  def addEnergy(y,x):
    global count 
    grid[y][x] += 1
    if grid[y][x] > 9 and (y,x) not in flashed:
      count += 1
      flashed.append((y,x))
      points = getPossiblePos(y,x)
      for y,x in points:
        addEnergy(y,x)
  
  for y in range(m):
    for x in range(n):
      addEnergy(y,x)
  for y,x in flashed:
    grid[y][x] = 0

print("\n".join(["".join([str(k) for k in n]) for n in grid]))
print(count,step)
