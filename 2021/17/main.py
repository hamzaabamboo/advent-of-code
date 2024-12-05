input = open('./input.txt').read()
 
target = ((185, 221), (-122, -74))
solutions = []
for vx in range(0, 1000):
  for vy in range(-200,200):
    position = [0,0]
    v = [vx, vy]
    step = 0;
    maxHeight = 0;
    def targetHit(position):
      return position[0] >= target[0][0] and position[0] <= target[0][1] and position[1] >= target[1][0] and position[1] <= target[1][1]
    while not targetHit(position):
      if ( target[1][1] - position[1] > 999 ): break;
      position[0] += v[0]
      position[1] += v[1]
      if v[0] > 0:
        v[0] -= 1
      elif v[0] < 0:
        v[0] += 1
      v[1] -= 1
      maxHeight = max(maxHeight, position[1])
      step += 1
    if targetHit(position):
      # print("solution found", (vx,vy), step, "steps")
      solutions.append((vx,vy, step, maxHeight))
print(solutions)
print((min(solutions, key=lambda x : x[0])[0],max(solutions, key=lambda x : x[0])[0]), (min(solutions, key=lambda x : x[1])[1], max(solutions, key=lambda x : x[1])[1]), max(solutions, key=lambda x : x[2])[2])
print(len(solutions))