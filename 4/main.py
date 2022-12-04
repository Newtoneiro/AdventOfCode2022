import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

def main1():
  sum = 0
  with open(filename) as f:
    for line in f:
      range1, range2 = line.strip().split(',')
      range1_a, range1_b = [int(_) for _ in range1.split('-')]
      range2_a, range2_b = [int(_) for _ in range2.split('-')]
      a = [_ for _ in range(range1_a, range1_b + 1)]
      b = [_ for _ in range(range2_a, range2_b + 1)]
      if len(set(a + b)) != len(a) + len(b):
        sum += 1
              
  return sum 

if __name__ == "__main__":
  print(main1())
