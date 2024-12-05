input = open("./input.txt").read()
positions = [int(n) for n in input.split(",")]
avg = sum(positions)/len(positions)
minPos = positions[0]
minEnergy = 99e9
def magic(n):
  return n * (n+1) / 2
for startingPos in range(min(positions), max(positions)):
  energyUsed = sum([magic(abs(pos - startingPos)) for pos in positions])
  if energyUsed < minEnergy:
    minEnergy = energyUsed
    minPos = startingPos

print(minEnergy, minPos)