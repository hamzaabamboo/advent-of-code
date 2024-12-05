lines = open('./input.txt').readlines()
accH = 0
accV = 0
aim = 0
for l in lines:
  cmd, x = l.split(" ");
  n = int(x)
  if cmd == "forward":
    accH += n
    accV += aim*n
  elif cmd == "up":
    aim -= n
  elif cmd == "down":
    aim += n
print(accH * accV)