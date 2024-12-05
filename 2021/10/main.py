input = open("./input.txt").read() 
lines = input.split('\n')
opening = '([{<'
closing = ')]}>'
pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
errorScore = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
autoCompleteScore = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
def getScore(line):
  q = []
  for item in line:
    if item in opening:
      q.append(item)
    elif item in closing and pairs[q[-1]] == item:
      q.pop()
    else:
      # return errorScore[item]
      return 0
  # if (len(q) > 0): return 0
  score = 0
  while len(q) > 0:
    char = q.pop()
    score = score * 5 + autoCompleteScore[pairs[char]]
  return score

scores = [getScore(line) for line in lines]
validScores = [s for s in scores if s > 0]
print(sorted(validScores)[int(len(validScores) / 2)])