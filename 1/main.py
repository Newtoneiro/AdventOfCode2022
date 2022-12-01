import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

def main():
  top_max = [0, 0, 0]
  with open(filename) as f:
    sum = 0
    for line in f:
      line = line.strip()
      if not line:
        if sum > any(top_max):
          top_max.append(sum)
          top_max = sorted(top_max, reverse=True)
          top_max.pop()
        sum = 0
        continue
      sum += int(line)
  return top_max
      

if __name__ == "__main__":
  print(sum(main()))