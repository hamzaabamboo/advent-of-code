input = open("./input.txt").read()

algorithm = input.split('\n\n')[0].replace('\n', '')
image = [[0 if item == '.' else 1 for item in line] for line in input.split('\n\n')[1].split('\n')]

def pad(image, size = 2, padWith = 0):
  n = len(image)
  m = len(image[0])
  newImage = [[padWith for i in range(m + 2*size)] for i in range(n + 2*size)]
  for y in range(n):
    for x in range(m):
      newImage[y + size][x + size] = image[y][x]
  return newImage

def convolute(y,x,image, defaultBit = '0'):
    bitString = ''
    if y - 1 < 0 or x - 1 < 0: bitString += defaultBit
    else: bitString += str(image[y-1][x-1])
    if y - 1 < 0: bitString += defaultBit
    else: bitString += str(image[y-1][x])
    if y - 1 < 0 or x + 1 >= len(image[0]): bitString += defaultBit
    else: bitString += str(image[y-1][x+1])
    if x - 1 < 0: bitString += defaultBit
    else: bitString += str(image[y][x-1])
    bitString += str(image[y][x])
    if x + 1 >= len(image[0]): bitString += defaultBit
    else: bitString += str(image[y][x+1])
    if y + 1 >= len(image) or x - 1 < 0: bitString += defaultBit
    else: bitString += str(image[y+1][x-1])
    if y + 1 >= len(image): bitString += defaultBit
    else: bitString += str(image[y+1][x])
    if y + 1 >= len(image) or x + 1 >= len(image[0]): bitString += defaultBit
    else: bitString += str(image[y+1][x+1])
    # print((y,x), bitString, int(bitString, base=2))
    return 0 if algorithm[int(bitString, base=2)] == '.' else 1

def printImage(image):
  print("\n".join([ "".join(['#' if a == 1 else '.' for a in row]) for row in image ]))

# print(sum([sum(row) for row in image]))
for step in range(50):
  image = pad(image, 2, 0 if step%2 == 0 else 1)
  newImage = image
  res = [[0 for _ in range(len(newImage[0]))] for a in range(len(newImage))]
  # printImage(newImage)
  for y in range(len(newImage)):
    for x in range(len(newImage[0])):
      res[y][x] = convolute(y,x,newImage, '0' if step%2 == 0 else '1')
  image = res
  # printImage(res)

print(sum([sum(row) for row in res]))
