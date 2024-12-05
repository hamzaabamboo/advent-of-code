input = open("./input.txt").read()

marks, instructions = input.split('\n\n')
marks = [tuple([int(n) for n in line.split(',')][::-1]) for line in marks.split('\n')]
instructions = [tuple(instruction.replace("fold along ", "").split("=")) for instruction in instructions.split('\n')]
m = max(marks, key=lambda t: t[0])[0] + 1
n = max(marks, key=lambda t: t[1])[1] + 1
print(len(marks))
print(m, 'x',n)
print(instructions)
board = [ [ '#' if (y,x) in marks else '.' for x in range(n)] for y in range(m)] 
for instruction in instructions:
  axis, position = instruction
  position = int(position)
  if axis == 'y':
    foldSize = len(board) - position - 1
    offset = position - foldSize
    newBoard = [[board[y][x] if y < position - foldSize else ( '#' if (board[y][x] == '#' or board[-(y-offset)-1][x] == '#') else '.' ) for x in range(len(board[0])) ] for y in range(len(board) - foldSize - 1)]
  elif axis == 'x':
    foldSize = len(board[0]) - position - 1
    offset = position - foldSize
    newBoard = [[board[y][x] if x < position - foldSize else ('#' if ( board[y][x] == '#' or board[y][-(x - offset)-1] == '#') else '.' ) for x in range(len(board[0]) - foldSize - 1) ] for y in range(len(board))]
  board = newBoard
print("\n".join([ "".join(['■' if a == '#' else '.' for a in path]) for path in board ]))