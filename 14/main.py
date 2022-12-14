import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

def main():
  cave = set()
  with open(filename) as f:
    for line in f:
      line = line.strip()
      points = line.split(' -> ')
      last_coords = ()
      for point in points:
        coords = [int(x) for x in point.split(',')]
        if last_coords:
          if abs(last_coords[0] - coords[0]) == 0:
            for y in range(min(last_coords[1], coords[1]), max(last_coords[1], coords[1]) + 1):
              cave.add((y, coords[0]))
          else:
            for x in range(min(last_coords[0], coords[0]), max(last_coords[0], coords[0]) + 1):
              cave.add((coords[1], x))
        last_coords = coords
  
  start = len(cave)
  floor_lvl = max([point[0] for point in cave]) + 2

  stop = False
  while not stop:
    sand_pos = (0, 500)
    can_move = True
    while can_move:
      # p1
      # if sand_pos[0] > 1000:
      #   stop = True
      #   can_move = False
      #p2
      if sand_pos[0] + 1 == floor_lvl:
        can_move = False

      elif (sand_pos[0] + 1, sand_pos[1]) not in cave:
        sand_pos = (sand_pos[0] + 1, sand_pos[1])
      elif (sand_pos[0] + 1, sand_pos[1] - 1) not in cave:
        sand_pos = (sand_pos[0] + 1, sand_pos[1] - 1)
      elif (sand_pos[0] + 1, sand_pos[1] + 1) not in cave:
        sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
      elif sand_pos == (0, 500):
        can_move = False
        stop = True
      else:
        can_move = False

    cave.add(sand_pos)
  
  end = len(cave)
  
  return end - start


if __name__ == "__main__":
  print(main())