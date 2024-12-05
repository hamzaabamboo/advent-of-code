input = open("./input.txt").read()
heightMap = [[int(n) for n in row] for row in input.split("\n")]
m = len(heightMap)
n = len(heightMap[0])
print(m,n)
lowSpots = []
for row in range(m):
  for col in range(n):
    cur = heightMap[row][col]
    if (row == 0 or cur < heightMap[row-1][col]) and (row == m - 1 or cur < heightMap[row+1][col]) and (col == 0 or cur < heightMap[row][col-1]) and (col == n-1 or cur < heightMap[row][col + 1]) : 
      lowSpots.append((row,col))
basinsMap = {}
for lowSpot in lowSpots:
  queue = [lowSpot]
  visited = []
  points = []
  while len(queue) > 0:
    row,col = queue.pop(0)
    if not (row,col) in points: points.append((row,col))
    if (row,col) in visited : continue
    else: visited.append((row,col))
    cur = heightMap[row][col]
    if (row > 0 and (cur < heightMap[row-1][col] and heightMap[row-1][col] != 9)):
      queue.append((row-1,col))
    if (row < m-1 and (cur < heightMap[row+1][col] and heightMap[row+1][col]  != 9)):
      queue.append((row+1,col))
    if (col > 0 and (cur < heightMap[row][col-1] and heightMap[row][col-1] != 9)):
      queue.append((row,col-1))
    if (col < n-1 and (cur < heightMap[row][col + 1] and heightMap[row][col+1] != 9)): 
      queue.append((row,col+1))
  basinsMap[lowSpot] = points
# print(lowSpots)
# print(sorted([len(basinsMap[key]) for key in basinsMap], reverse=1))
print(sum([heightMap[row][col] + 1 for row,col in lowSpots]))

# for key in basinsMap:
#   def getSymbol(row,col):
#     if (row,col) in basinsMap[key]:
#       return "-"
#     n = heightMap[row][col];
#     if n == 9: return "X"
#     return str(n)
#   # print("\n".join(["".join([getSymbol(row,col) for col in range(n)]) for row in range(m)]))
#   # print("\n")