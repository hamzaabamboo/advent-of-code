input = open("./input.txt").read()
scores = [[[0 for _ in range(10)] for n in range(21)],[[0 for _ in range(10)] for n in range(21)]]
scores[0][0][7] = 1
scores[0][1][8] = 1
scores[0][2][9] = 1
scores[1][0][0] = 1
scores[1][1][1] = 1
scores[1][2][2] = 1


def printScores(scores):
  for player in range(2):
    print("Player ", player)
    print("\n".join([str(n + 1) + ":" + ", ".join([ str(scores[player][n][a]) for a in range(len(scores[player][n]))]) for n in range(len(scores[player]))]))  

# while sum([sum(p) for p in scores[0]]) != 0 or sum([sum(p) for p in scores[1]]):
for a in range(21):
  newScore = [[[0 for a in s] for s in p] for p in scores]
  for player in range(len(scores)):
    for score in range(21):
      for position in range(10):
        newScore[player][score][position] = scores[player][score - 1][(position - 1) % 10] + scores[player][score - 2][(position - 2) % 10] if score > 0 else 0 + scores[player][score - 3][(position - 3) % 10] if score > 1 else 0
        if score == 20: newScore[player][score][position] += scores[player][score][position]
  scores = newScore
printScores(scores)