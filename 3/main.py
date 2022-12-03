import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

def getAscii(char):
  if char == char.upper():
    return ord(char) - 38
  else:
    return ord(char) - 96

# 1
def main1():
  sum = 0
  with open(filename) as f:
    for line in f:
      line = line.strip()
      first, second = line[0: int(len(line)/2)], line[int(len(line)/2):]
      
      for a in first:
        if a in second:
          sum += getAscii(a)
          break
          
  return sum 

# 2
def main2():
  sum = 0
  with open(filename) as f:
    for line1 in f:
      line2 = f.readline()
      line3 = f.readline()
      for a in line1:
        if a in line2 and a in line3:
          sum += getAscii(a)
          break
  return sum  

if __name__ == "__main__":
  print(main1())
  print(main2())
