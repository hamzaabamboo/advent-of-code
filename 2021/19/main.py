input = open("./input.txt").read()
scanners = [[tuple([int(i) for i in coords.split(',')]) for coords in a.split("\n")[1:]] for a in input.split("\n\n")]
distances = {}
def findDistance(p1, p2 = (0,0,0)):
  return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2 )** 1/2
for idx in range(len(scanners)):
  distances[idx] = []
  for p1 in scanners[idx]:
    for p2 in scanners[idx]:
      if (p1 == p2): continue
      distances[idx].append(findDistance(p1, p2))
allDistances = set()
for key in distances:
  allDistances.update(distances[key])

print(len(allDistances))