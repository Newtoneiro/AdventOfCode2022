import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

def getTrees():
  trees = []
  with open(filename) as f:
    for line in f:
      line = line.strip()
      row = []
      for tree in line:
        row.append(int(tree))
      trees.append(row)
  return trees

def main1():
  trees = getTrees()
  
  sum = 0
  for row in range(0, len(trees)):
    for col in range(0, len(trees[row])):
      # left
      visible_left = True
      if col != 0 and trees[row][col] <= max(trees[row][:col]):
        visible_left = False

      # right
      visible_right = True
      if col != len(trees[row]) - 1 and trees[row][col] <= max(trees[row][col+1:len(trees[row])]):
        visible_right = False
      
      # top
      visible_top = True
      if row != 0 and trees[row][col] <= max([row[col] for row in trees[:row]]):
        visible_top = False

      # bottom
      visible_bottom = True
      if row != len(trees) - 1 and trees[row][col] <= max([row[col] for row in trees[row+1:len(trees)]]):
        visible_bottom = False

      if any([visible_bottom, visible_left, visible_right, visible_top]):
        sum += 1
    
  return sum

def main2():
  trees = getTrees()
  
  max_vision = 0
  for row in range(0, len(trees)):
    for col in range(0, len(trees[row])):
      # left
      score_left = 0
      for compare_col in range(1, col+1):
        score_left += 1
        if trees[row][col-compare_col] >= trees[row][col]:
          break
      
      # right
      score_right = 0
      for compare_col in range(col+1, len(trees[row])):
        score_right += 1
        if trees[row][compare_col] >= trees[row][col]:
          break
      
      # top
      score_top = 0
      for compare_row in range(1, row+1):
        score_top += 1
        if trees[row - compare_row][col] >= trees[row][col]:
          break
      
      # bottom
      score_bottom = 0
      for compare_row in range(row+1, len(trees)):
        score_bottom += 1
        if trees[compare_row][col] >= trees[row][col]:
          break
      
      score = score_left * score_bottom * score_right * score_top
      if score > max_vision:
        max_vision = score
    
  return max_vision

if __name__ == "__main__":
  print(main1())
  print(main2())
