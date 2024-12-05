input = open('./input.txt').read()
inputs = [[[n for n in line.split("|")[0].strip().split(" ")], [n for n in line.split("|")[1].strip().split(" ")]] for line in input.split('\n')]
print(inputs[:3])
acc = 0
for line in inputs:
  test, output = line
  inputMap = {}
  queue = sorted(test, key=lambda x: len(x))
  while len(queue) > 0:
    cfg = queue.pop(0)
    if (len(cfg) == 2): inputMap[1] = cfg;
    elif (len(cfg) == 3): inputMap[7] = cfg;
    elif (len(cfg) == 4): inputMap[4] = cfg;
    elif (len(cfg) == 5) and 7 in inputMap and all(s in cfg for s in inputMap[7]):
        inputMap[3] = cfg
    elif (len(cfg) == 6) and 3 in inputMap and all(s in cfg for s in inputMap[3]):
        inputMap[9] = cfg
    elif (len(cfg) == 7): inputMap[8] = cfg;
    elif 9 in inputMap and (len(cfg) == 5 and 3 in inputMap  and cfg != inputMap[3]): 
      if all(s in inputMap[9] for s in cfg):
        inputMap[5] = cfg
      else:
        inputMap[2] = cfg
    elif 5 in inputMap and (len(cfg) == 6 and cfg != inputMap[9]): 
      if 5 in inputMap and all(s in cfg for s in inputMap[5] ):
        inputMap[6] = cfg
      else:
        inputMap[0] = cfg
    else:
      queue.append(cfg)
  newMap = {}
  for key in inputMap:
    newKey = "".join(sorted(inputMap[key]))
    newMap[newKey] = key
  
  digits = ""
  for k in output:
    digits += str(newMap["".join(sorted(k))])
  acc += int(digits)
print(acc)