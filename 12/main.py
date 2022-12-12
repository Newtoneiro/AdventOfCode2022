import os
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

def main():
  map = []
  start = exit = 0

  queue = deque()
  with open(filename) as f:
    for row_no, line in enumerate(f):
      line = line.strip()
      row = []
      for col_no, char in enumerate(line):
        if char == "S" or char == "a":
          start = (row_no, col_no)
          queue.append((0, row_no, col_no))
        if char == "E":
          exit = (row_no, col_no)
        row.append(char)
      map.append(row)
  
  map[start[0]][start[1]] = 'a'
  map[exit[0]][exit[1]] = 'z'
  
  # bfs
  visited = {start}
  
  while len(queue) != 0:
    distance, row, column = queue.popleft()
    for neighbour in getNeighbours(row, column, map):
      if neighbour == exit:
        return distance + 1
      if neighbour not in visited:
        queue.append((distance + 1, neighbour[0], neighbour[1]))
      visited.add(neighbour)

def getNeighbours(row, col, map):
  neighbours = []
  cur_char = map[row][col]
  if row > 0 and ord(map[row-1][col]) - ord(cur_char) <=1:
    neighbours.append((row-1, col))
  if row < len(map)-1 and ord(map[row+1][col]) - ord(cur_char) <=1:
    neighbours.append((row+1, col))
  if col > 0 and ord(map[row][col-1]) - ord(cur_char) <=1:
    neighbours.append((row, col-1))
  if col < len(map[row])-1 and ord(map[row][col+1]) - ord(cur_char) <=1:
    neighbours.append((row, col+1))
  return neighbours

if __name__ == "__main__":
  print(main())
