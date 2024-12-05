f = open("./input.txt")


def is_row_safe(row):
  if len(row) == 1: 
      return True
  is_safe = True
  is_asc = row[1] - row[0] > 0 
  for i in range(1, len(row)):
      diff = row[i] - row[i-1] if is_asc else row[i-1] - row[i]
      if (diff <= 0 or diff > 3) : 
        is_safe = False;
  return is_safe

def is_row_safe_dampened(row): 
  if is_row_safe(numbers):
    return True
  for i in range(0, len(numbers)):
    tmp = row[0:i] + row[i+1: len(numbers)]
    if is_row_safe(tmp):
      return True 
      
safe = 0;
for line in f.readlines():
    numbers = [int(n) for n in line.split()]
    if is_row_safe_dampened(numbers):
      safe = safe + 1; 


print(safe)