input = open('./input.txt').read()
template, pairs = input.split("\n\n")
pairsMap = {}
for line in pairs.split("\n"):
  start, end = line.split(" -> ")
  pairsMap[start] = end

countMap = {}
for i in range(len(template)-1): 
  word = template[i:i+2]
  if not word in countMap: countMap[word] = 0
  countMap[word] += 1

for key in pairsMap:
  if not key in countMap: countMap[key] = 0

print(countMap)

for step in range(40):
  newMap = {}
  for key in pairsMap:
    newMap[key] = 0
  for key in pairsMap:
    newMap[key[0] + pairsMap[key]] += countMap[key]
    newMap[pairsMap[key] + key[1]] += countMap[key]
  countMap = newMap
  print(countMap)

letters = set()
for pair in countMap:
  letters.add(pair[0])
  letters.add(pair[1])

letterMap = {}
for letter in letters:
  pairs = [k for k in countMap.keys() if k[0] == letter]
  letterMap[letter] = sum([countMap[k] if k[0] != k[1] else countMap[k]  for k in pairs])
letterMap[template[-1]] += 1
print(letterMap)
print(max(letterMap.values()) - min(letterMap.values()))