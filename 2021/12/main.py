input = open("./input.txt").read()

links = {}
allNodes = set()
for link in input.split("\n"):
  start,end = link.split("-")
  allNodes.add(start)
  allNodes.add(end)
  if not start in links: 
    links[start] = set()
  if not end in links: 
    links[end] = set()
  links[start].add(end)
  if (start != 'start') : links[end].add(start)

visits = []
for luckyNode in [a for a in allNodes if not a[0].isupper() and a != 'start' and a != 'end']:
  visit = {}
  for node in allNodes:
    if ( node == 'start' or node == 'end'): visit[node] = 1
    elif ( node[0].isupper() ): visit[node] = None
    elif (node == luckyNode): visit[node] = 2
    else: visit[node] = 1
  visits.append(visit)

print(visits)
def findPath(startNode, visits):
  paths = []
  if (startNode not in links): return []
  if (startNode == 'end'): return [()]

  remainingVisits = visits.copy()
  if (remainingVisits[startNode] != None ): 
    remainingVisits[startNode] -= 1
    if (remainingVisits[startNode] == 0):
      del remainingVisits[startNode]
  # print(startNode, remainingVisits)
  for node in links[startNode]: 
    if not node in remainingVisits: continue
    subPaths = findPath(node, remainingVisits)
    for subPath in subPaths:
      paths.append(tuple([node]) + subPath)
  return paths

def findAllPaths():
  paths = [ findPath('start', visit) for visit in visits]
  result = []
  for path in paths:
    result += path
  return set(result)
  
result = findAllPaths()
# print("\n".join([ ",".join(path) for path in result ]))
print(len(result))