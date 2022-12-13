import os
from itertools import zip_longest

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')


def compare(x, y):
  if isinstance(x, int):
    if isinstance(y, int):
      return x - y
    else:
      return compare([x], y)
  else:
    if isinstance(y, int):
      return compare(x, [y])
  
  for element1, element2 in zip(x, y):
    v = compare(element1, element2)
    if v:
      return v
  
  return len(x) - len(y)
    
  
def main():
  sum = 0
  with open(filename) as f:
    lines = f.readlines()
    for num, (line1, line2, _) in enumerate(grouper(3, lines)):
      line1, line2 = line1.strip(), line2.strip()
      line1 = eval(line1)
      line2 = eval(line2)
      if (compare(line1, line2) < 0):
        sum += num + 1
      
  return sum

def main2():
  i2 = 1
  i6 = 2
  with open(filename) as f:
    lines = f.readlines()
    for line in lines:
      line = line.strip()
      if line:
        line = eval(line)
        if compare(line, [[2]]) < 0:
          i2 += 1
          i6 += 1
        elif compare(line, [[6]]) < 0:
          i6 += 1
  return i2 * i6


if __name__ == "__main__":
  print(main())
  print(main2())