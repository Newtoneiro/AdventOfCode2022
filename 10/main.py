import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

class Cycle:
  def __init__(self):
    self.cycle = 0
    self.register_val = 1
    #p1
    self.snapshot_values = [20, 60, 100, 140, 180, 220]
    self.sum = 0
    #p2
    self.screen = [['.' for i in range(40)] for j in range(6)]
    self.row = -1

  def noop(self):
    self.cycle += 1
    self.snapshot()

  def addx(self, val):
    self.cycle += 1
    self.snapshot()
    self.cycle += 1
    self.snapshot()
    self.register_val += val
  
  def snapshot(self):
    if self.cycle in self.snapshot_values:
      self.sum += (self.cycle * self.register_val)
    if (self.cycle - 1) % 40 == 0:
      self.row += 1
    
    cur_pixel = (self.cycle - 1) % 40
    
    if (abs(cur_pixel - self.register_val) <= 1):
      self.screen[self.row][cur_pixel] = "#"
  
  def printScreen(self):
    for row in self.screen:
      print(row)

def main():
  cycle = Cycle()
  with open(filename) as f:
    for line in f:
      line = line.strip()
      args = line.split(' ')
      if args[0] == "noop":
        cycle.noop()
      elif args[0] == "addx":
        cycle.addx(int(args[1]))
  
  cycle.printScreen()
  return cycle.sum     

if __name__ == "__main__":
  print(main())