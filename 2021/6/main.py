input = open("./input.txt").read()
fishes = [int(n) for n in input.split(",")]
fishmap = { 0: 0, 1: 0, 2: 0, 3: 0 ,4: 0, 5: 0, 6: 0, 7:0, 8:0 }
for counter in fishes:
  fishmap[counter] += 1

for i in range(256):
  tmp = fishmap[0]
  for i in range (8):
    fishmap[i] = fishmap[i+1]
  fishmap[8] = tmp
  fishmap[6] += tmp
print(sum(fishmap.values()))