res = open("./input.txt").read()
lines = [[a.split(",") for a in n.split(' -> ')] for n in res.split('\n')]
box = [[0 for _ in range(1000)] for _ in range(1000)]

for line in lines:
  start, end = line
  startX, startY = start
  endX, endY = end
  startX, startY, endX, endY = int(startX), int(startY), int(endX), int(endY)
  if startX == endX:
    start,end = (startY, endY) if startY < endY else (endY, startY) 
    for a in range(start, end + 1):
      box[a][startX] += 1;
  elif startY == endY:
    start,end = (startX, endX) if startX < endX else (endX, startX)
    for a in range(start, end + 1):
      box[startY][a] += 1;
  elif (startX < endX and startY < endY) or (endX < startX and endY < startY):
    dx = endX - startX if startX < endX else startX - endX 
    x = startX if startX < endX else endX
    y = startY if startY < endY else endY
    for a in range(0,dx + 1):
      box[y + a][x + a] += 1
  elif (startX < endX and startY > endY) or (endX < startX and endY > startY):
    dx = endX - startX if startX < endX else startX - endX 
    x = startX if startX < endX else endX
    y = startY if startY > endY else endY
    for a in range(0, dx + 1):
      box[y - a][x + a] += 1

acc = 0;
for row in box:
  for a in row:
    if a > 1: acc += 1
print(acc)
# print("\n".join(["".join([ str(a) if a != 0 else "-" for a in row[:1000]]) for row in box[:1000]]))