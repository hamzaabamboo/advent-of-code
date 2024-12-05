import json;
from math import floor, ceil
input = open("./input.txt").read()

class TreeNode:
   def __init__(self, data, parent = None):
      self.left = None
      self.right = None
      self.parent = parent
      self.data = data
   def magnitude(self):
     if type(self.data) == int: return self.data
     return 3 * self.left.magnitude() + 2 * self.right.magnitude()
   def __str__(self):
     if type(self.data) == int:
       return str(self.data)
     line = '['
     line += str(self.left)
     line += ','
     line += str(self.right)
     line += ']'
     return line

def plantTree(line, parent = None):
  if type(line) == int:
    return TreeNode(line, parent)
  node = TreeNode(None, parent)
  node.left = plantTree(line[0], node)
  node.right = plantTree(line[1], node)
  return node

def add(a, b):
  node = TreeNode(None)
  node.left = a
  node.right = b
  a.parent = node
  b.parent = node
  prev = None
  while True:
    explode(node)
    split(node)
    if (prev == str(node)):
      break;
    prev = str(node)
  return node

def getRightMostNode(node):
  c = node
  while c:
    if type(c.data) == int:
      return c
    c = c.right

def getLeftMostNode(node):
  c = node
  while c:
    if type(c.data) == int:
      return c
    c = c.left
def getRightNode(node):
  # print("Finding right for", node)
  if type(node.data) == int:
      return node
  currentNode = node
  while currentNode:
    # print("Current", currentNode)
    if type(currentNode.data) == int:
      return currentNode
    if currentNode.parent and currentNode.parent.right != currentNode:
      if currentNode.parent.right.left and type(currentNode.parent.right.left.data) == int:
        return currentNode.parent.right.left
      return getLeftMostNode(currentNode.parent.right)
    else:
      currentNode = currentNode.parent
      

def getLeftNode(node):
  # print("Finding left for", node)
  currentNode = node
  while currentNode:
    # print("Current", currentNode)
    if type(currentNode.data) == int:
      return currentNode
    if currentNode.parent and currentNode.parent.left != currentNode:
      if currentNode.parent.left.right and type(currentNode.parent.left.right.data) == int:
        return currentNode.parent.left.right
      return getRightMostNode(currentNode.parent.left)
    else:
      currentNode = currentNode.parent
      
def explode(node, depth = 0):
  if type(node.data) == int: return node
  elif type(node.left.data) == int and type(node.right.data) == int and depth >= 4:
    # print("Exploding", node)
    rightNode = getRightNode(node)
    leftNode = getLeftNode(node)
    # print("Exploding", node, leftNode, rightNode)
    if leftNode: leftNode.data += node.left.data
    if rightNode: rightNode.data += node.right.data
    return TreeNode(0, node.parent)
  else:
    node.left = explode(node.left, depth+1)
    node.right = explode(node.right, depth+1)
    return node 

def split(node, parent = None):
    current = node
    stack = [] # initialize stack
    done = 0  
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            if type(current.data) == int:
              if current.data >= 10:
                # print("Splitting", node)
                newNode = plantTree([floor(current.data / 2), ceil(current.data / 2)], current.parent) 
                if current.parent:
                  if current.parent.left == current: current.parent.left = newNode
                  elif current.parent.right == current: current.parent.right = newNode
                return
            current = current.right
        else:
            break
        
       
# print(explode(plantTree(json.loads('[[6,[5,[4,[3,2]]]],1]'))))
# print(explode(plantTree(json.loads('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'))))
# print(plantTree(json.loads('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')).magnitude())

items = [json.loads(l) for l in input.split("\n")]
# currentSum = items[0]
# for item in items[1:]:
#   print("Add",currentSum, "to", item)
#   currentSum = add(currentSum, item)
#   print("Current Sum", currentSum)

maxMag = 0
for a in items:
  for b in items:
    maxMag = max(maxMag, add(plantTree(a),plantTree(b)).magnitude(), add(plantTree(b),plantTree(a)).magnitude())

print(maxMag)

# print("a", currentSum.magnitude())