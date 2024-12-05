import re

f = open("./input.txt")

everything = f.read()
dos = [re.split("don't\(\)", r)[0] for r in re.split("do\(\)", everything)]
s = 0
for things in dos:
    matches = re.findall("mul\((\d+),(\d+)\)", things)
    s = s + sum([int(a) * int(b) for (a, b) in matches])

print(s)
