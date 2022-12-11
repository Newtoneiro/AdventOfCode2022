import os
from math import prod

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

global mod
mod = prod([19, 13, 5, 7, 17, 2, 3, 11])  # To avoid extremaly big worry levels, we can modulo them by common divider 
                                          # (in that case for simplicity's sake - product of all the modulos)

class Monkey:
  def __init__(self, items, operation, test, monkey_true, monkey_false, worry_flag):
    self.items = items
    self.operation = operation
    self.test = test
    self.monkey_true = monkey_true
    self.monkey_false = monkey_false
    self.worry_flag = worry_flag

    self.time_inspected = 0
  
  def give(self, item):
    self.items.append(item)
  
  def round(self):
    results = []
    for item in self.items:
      self.time_inspected += 1
      value = self.operation(item)
      if not self.worry_flag:
        value = int(value / 3)
      else:
        value = value % mod
      if self.test(value):
        results.append((value, self.monkey_true))
      else:
        results.append((value, self.monkey_false))
    self.items = []
    return results
  
def main(rounds, worry_flag):
  monkey0 = Monkey([93, 98], lambda x: x * 17, lambda x: x % 19 == 0, 5, 3, worry_flag)
  monkey1 = Monkey([95, 72, 98, 82, 86], lambda x: x + 5, lambda x: x % 13 == 0, 7, 6, worry_flag)
  monkey2 = Monkey([85, 62, 82, 86, 70, 65, 83, 76], lambda x: x + 8, lambda x: x % 5 == 0, 3, 0, worry_flag)
  monkey3 = Monkey([86, 70, 71, 56], lambda x: x + 1, lambda x: x % 7 == 0, 4, 5, worry_flag)
  monkey4 = Monkey([77, 71, 86, 52, 81, 67], lambda x: x + 4, lambda x: x % 17 == 0, 1, 6, worry_flag)
  monkey5 = Monkey([89, 87, 60, 78, 54, 77, 98], lambda x: x * 7, lambda x: x % 2 == 0, 1, 4, worry_flag)
  monkey6 = Monkey([69, 65, 63], lambda x: x + 6, lambda x: x % 3 == 0, 7, 2, worry_flag)
  monkey7 = Monkey([89], lambda x: x * x, lambda x: x % 11 == 0, 0, 2, worry_flag)

  monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
  for i in range(rounds):
    for monkey in monkeys:
      results = monkey.round()
      for result in results:
        monkeys[result[1]].give(result[0])
    print(f"[{i}/{rounds}]")
  
  times_inspected = [monkey.time_inspected for monkey in monkeys]
  times_inspected.sort()
  times_inspected.reverse()
  return times_inspected[0] * times_inspected[1]

if __name__ == "__main__":
  print(main(20, 0))
  print(main(10000, 1))