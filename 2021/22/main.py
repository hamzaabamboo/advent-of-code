input = open("./input.txt").read()
commands = [line for line in input.split("\n")]

on = set()
for command in commands:
  action, area = command.split(" ")
  x,y,z = [tuple([ int(b) for b in a.split("=")[1].split('..')]) for a in area.split(",")]
  coordinates = []
  for a in range(x[0], x[1] + 1):
    for b in range(y[0], y[1] + 1):
      for c in range(z[0], z[1] + 1):
        coordinates.append((a,b,c))
  if (action == 'on'): 
    on.update(coordinates)
  else:
    on.difference_update(coordinates)
  # print(on)
print(len(on))