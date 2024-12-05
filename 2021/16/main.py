from functools import reduce
input = open('./input.txt').read()
def convert(a):
  n = int(a, base=16)
  binNo = bin(n)[2:]
  extraPadding = len(a) * 4 -  len(binNo)
  return ''.join(['0' for _ in range(extraPadding)]) + binNo

def parseNormalPacketContent(p):
  version = int(p[:3], base=2)
  packetType = int(p[3:6], base=2)
  isOperator = packetType != 4
  current = p[6:]
  val = ""
  packetLength = 6
  while (current[0] == '1'):
    val += current[1:5]
    current = current[5:]
    packetLength += 5
  val += current[1:5]
  packetLength += 5
  return {
      "version": version,
      "packetType": packetType,
      "length": packetLength,
      "value": int(val, base=2)
  }
  
def parsePacket(p):
  version = int(p[:3], base=2)
  packetType = int(p[3:6], base=2)
  isOperator = packetType != 4
  packetLength = 6
  ret = {
      "version": version,
      "packetType": packetType,
  }
  if isOperator:
    mode = p[6]
    subpackets = []
    if mode == '0':
      length = int(p[7:22], base = 2)
      i = 0
      print('Mode 0:', length, 'bytes')
      while i < length - 1:
        newPacket = parsePacket(p[22 + i: 22 + length])
        i += newPacket["length"]
        subpackets.append(newPacket)
      ret['length'] = 22 + i
    else: 
      length = int(p[7:18], base = 2)
      currentIdx = 18
      print('Mode 1:', length, 'subpackets')
      while len(subpackets) < length:
        newPacket = parsePacket(p[currentIdx:])
        currentIdx += newPacket["length"]
        subpackets.append(newPacket)
      ret['length'] = currentIdx
    ret['subpackets'] = subpackets
  else: 
    tmp = parseNormalPacketContent(p)
    ret['value'] = tmp["value"]
    ret['length'] = tmp["length"]

  print(ret)
  return ret

def evaluatePacket(p):
  pType = p["packetType"]
  if pType == 4: return p["value"]
  subpackets = [evaluatePacket(a) for a in p["subpackets"]];
  if pType == 0:
    return sum(subpackets)
  elif pType == 1:
    return reduce((lambda x, y: x * y), subpackets)
  elif pType == 2:
    return min(subpackets)
  elif pType == 3:
    return max(subpackets)
  elif pType == 5:
    return 1 if subpackets[0] > subpackets[1] else 0
  elif pType == 6:
    return 1 if subpackets[0] < subpackets[1] else 0
  elif pType == 7:
    return 1 if subpackets[0] == subpackets[1] else 0


pkt = parsePacket(convert(input))
print(pkt)
print(evaluatePacket(pkt))
q = []
q.append(pkt)
a = 0
while len(q) > 0:
  pkt = q.pop(0)
  a += pkt['version']
  q += pkt['subpackets'] if 'subpackets' in pkt else []