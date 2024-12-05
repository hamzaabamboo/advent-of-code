lines = [n for n in open("./input.txt").read().split('\n\n')]
bingoOrder = lines[0].split(',')
bingoBoards = [ [ [ n for n in row.split(' ') if n != ''] for row in board.split('\n') ] for board in lines[1:]]

print(len(bingoOrder), len(bingoBoards))
def isThatBoardWinning(board, pickedNumbers):
  if len(pickedNumbers) < 5: return False
  aSet = set(pickedNumbers);
  for row in board:
    if set(row) < aSet: return True
  for col in range(len(board[0])):
    line = {board[n][col] for n in range(len(board[0]))}
    if line < aSet: return True
  return False

lastWinner = None;
players = [board for board in bingoBoards]
def findWinnerPlease():
  for i in range(5, len(bingoOrder)): 
    win = []
    for idx in range(0, len(players)):
      if isThatBoardWinning(players[idx], bingoOrder[:i]):
         win.append(idx)
    # print(len(players))
    if (len(players) == 1 and len(win) == 1): return (players[0], bingoOrder[:i])
    for i in range(len(win)):
      lastWinner = players.pop(win[i] - i)
  
ourLuckyWinner, numberUsed = findWinnerPlease();
acc = 0
notSelected = []
for row in ourLuckyWinner:
  for n in row:
    # print(n, numberUsed)
    if not (n in numberUsed):
      acc += int(n)
      notSelected.append(n)
print(notSelected, sum([int(n) for n in notSelected]))
print(numberUsed[-1], acc * int(numberUsed[-1]))