import functools
import math

f = open("./input.txt")

raw = f.read()

rules, pages = raw.split("\n\n")

m = {}
for rule in rules.split():
    first, second = (int(a) for a in rule.split("|"))
    if not first in m:
        m[first] = []
    m[first].append(second)


def compare(a: int, b: int):
    if a in m and b in m[a]:
        return -1
    elif b in m and a in m[b]:
        return 1
    return 0


q1 = 0
q2 = 0
for page in pages.split():
    ns = [int(a) for a in page.split(",")]
    sortedns = sorted(ns, key=functools.cmp_to_key(compare))
    if ns == sortedns:
        q1 += ns[math.floor(len(ns) / 2)]
    else:
        q2 += sortedns[math.floor(len(ns) / 2)]

print(q1)
print(q2)
