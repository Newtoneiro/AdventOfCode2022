import os
import itertools

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

rock1 = [(0, 0), (0, 1), (0, 2), (0, 3)]
rock2 = [(1, 0), (1, 1), (0, 1), (1, 2), (2, 1)]
rock3 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
rock4 = [(0, 0), (1, 0), (2, 0), (3, 0)]
rock5 = [(0, 0), (1, 0), (0, 1), (1, 1)]
rocks = [rock1, rock2, rock3, rock4, rock5]

def main():
  jets = []
  with open(filename) as f:
    for line in f:
      line = line.strip()
      for char in line:
        jets.append(char)
  
  occupied_spaces = set([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
  i = 0
  cur_jet = 0
  for rock in itertools.cycle(rocks):
    pos = (max([space[0] for space in occupied_spaces]) + 4, 2)
    while not any([(pos[0] + rock_part[0] - 1, pos[1] + rock_part[1]) in occupied_spaces for rock_part in rock]):
      column = pos[1]
      if jets[cur_jet] == '>':
        furthest_right = max([column + rock_part[1] for rock_part in rock])
        if furthest_right < 6:
          column = column + 1
      elif jets[cur_jet] == '<':
        column = max([column - 1, 0])
      if ((pos[0] - 1, column) not in occupied_spaces):
        pos = (pos[0] - 1, column)
      else:
        pos = (pos[0], column)
      cur_jet += 1
      cur_jet = cur_jet % len(jets)
    # Set the rock
    for rock_part in rock:
      occupied_spaces.add((pos[0] + rock_part[0], pos[1] + rock_part[1]))
    i += 1
    if i == 2022:
      break
  
  return max([space[0] for space in occupied_spaces])

if __name__ == "__main__":
  print(main())


