res = open('./input.txt').read()
lines = [int(n) for n in res.split('\n')]
acc = 0
prev = lines[0] + lines[1] + lines[2]
for l in range(1, len(lines) - 2):
  currSum = lines[l] + lines[l+1] + lines[l+2]
  if currSum > prev:
    acc += 1
  prev = currSum

print(acc)