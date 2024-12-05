res = open('./input.txt').read()
lines = [n for n in res.strip().split('\n')]
counters = [[0,0] for i in range(12)]
for l in lines:
  for i in range(len(l)):
    counters[i][int(l[i])] += 1
gamma = 0
epsilon = 0
res = ""
for i in range(len(counters)):
  zeros, ones = counters[::-1][i]
  if zeros > ones:
    res += "0"
    epsilon += 2 ** i
  else:
    res += "1"
    gamma += 2 ** i
print(res)
print(gamma)
print(epsilon)
print(gamma * epsilon)


n = [n for n in lines]
for digit in range(len(n[0])):
  if (len(n) == 1): break;
  counter = [0,0];
  for num in n:
    counter[int(num[digit])] += 1
  zeros, ones = counter
  if zeros <= ones:
    n = [ a for a in n if a[digit] == "1"]
  else:
    n = [ a for a in n if a[digit] == "0"]
  print(len(n))
print(n)
a = "101110111101"
b = "011001010000"
# answer is a*b