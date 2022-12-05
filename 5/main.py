import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

STACKS_NUMBER = 9

def main(mode):
  stacks = [[] for _ in range(STACKS_NUMBER)]
  with open(filename) as f:
    for line in f:
      line = line.strip('\n')
      # Delimiter between stacks and set of moves
      if ('1' in line):
        break
      stack_no = 0
      for i, char in enumerate(line):
        i = i%4
        if i == 1:
          if char != ' ':
            stacks[stack_no].append(char)
          stack_no += 1
      
    for i in range(len(stacks)):
      stacks[i].reverse()
    
    for line in f:
      line = line.strip()
      if line == '':
        continue
      stuff = line.split(' ')
      amount, _from, _to = int(stuff[1]), int(stuff[3]), int(stuff[5])
      if mode == 1:
        for i in range(amount):
          crate = stacks[_from - 1].pop()
          stacks[_to - 1].append(crate)
      elif mode == 2:
        tmp = []
        for i in range(amount):
          tmp.append(stacks[_from - 1].pop())
        for i in range(len(tmp)):
          stacks[_to - 1].append(tmp.pop())

  output = ''
  for stack in stacks:
    output += stack[len(stack) - 1]
  return output

if __name__ == "__main__":
  print(main(2))
