import os
import re

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

Y=2000000

def main():
  sensors = set()
  beacons = set()
  with open(filename) as f:
    for line in f:
      line = line.strip()
      x = [int(x_.strip('x=')) for x_ in re.findall('x=.?\d*', line)]
      y = [int(y_.strip('y=')) for y_ in re.findall('y=.?\d*', line)]
      dist = abs(x[0] - x[1]) + abs(y[0] - y[1])
      sensors.add((x[0], y[0], dist))
      beacons.add((x[1], y[1]))
  
  def valid(x, y, s):
    for (sonar_x, sonar_y, dist) in s:
      dist_2 = abs(x - sonar_x) + abs(y - sonar_y)
      if dist_2 <= dist:
        return False
    return True

  #p1
  # sum = 0
  # for x in range(-int(1e7), int(1e7)):
  #   if not valid(x, Y, sensors) and (x, Y) not in beacons:
  #     sum += 1
  # return sum

  #p2
  found_p2 = False
  for (sonar_x , sonar_y, dist) in sensors:
    for dx in range(dist+2):
        dy = (dist+1)-dx
        for signx,signy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            x = sonar_x+(dx*signx)
            y = sonar_y+(dy*signy)
            if not(0 <= x <= 4000000 and 0 <= y <= 4000000):
              continue
            assert abs(x-sonar_x) + abs(y-sonar_y) == dist + 1
            if valid(x, y, sensors) and (not found_p2):
                return x*4000000 + y

if __name__ == "__main__":
  print(main())