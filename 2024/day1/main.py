f = open("./input.txt")

list1 = []
list2 = []
for line in f.readlines():
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))

slist1 = sorted(list1)
slist2 = sorted(list2)

differences = []
for i in range(len(list1)):
    differences.append(abs(slist1[i] - slist2[i]))

print(f"Part1 {sum(differences)}")

m = {key: 0 for key in list1}
for n in list2:
    if n in m:
        m[n] = m[n] + 1

print(f"Part2 {sum([ k * m[k] for k in m ])}")
