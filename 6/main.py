import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

def main(distinct_length):
  with open(filename) as f:
    marker = 0
    recent = []
    for c in f.read():
      recent.append(c)
      marker += 1
      if len(set(recent)) == distinct_length:
        break
      if len(recent) == distinct_length:
        recent.pop(0)
              
  return marker 

if __name__ == "__main__":
  print(main(4))
  print(main(14))
