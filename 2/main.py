import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

round_points = {"draw" : 3,
                "win" : 6,
                "lose" : 0}

beats = {"A": "C",
         "B": "A",
         "C": "B"}

#1
def main():
  shape_points = {"X" : 1,
                "Y" : 2,
                "Z" : 3}

  translation = {"X" : "A",
                "Y" : "B",
                "Z" : "C"}
                
  score = 0
  with open(filename) as f:
    for line in f:
      line = line.strip()
      elve, you = line.split(' ')
      #draw
      score += shape_points[you]
      if (elve == translation[you]):
        score += round_points["draw"]
      #win
      elif (beats[translation[you]] == elve):
        score += round_points["win"]
      #else lose (no points)
  return score

#2

def main2():
  shape_points = {"A" : 1,
                "B" : 2,
                "C" : 3}
  
  loses_against = {v : k for k, v in beats.items()}

  score = 0
  with open(filename) as f:
    for line in f:
      line = line.strip()
      elve, you = line.split(' ')
      # lose
      if you == "X":
        score += shape_points[beats[elve]]
      # draw
      elif you == "Y":
        score += shape_points[elve]
        score += round_points["draw"]
      # win
      else:
        score += shape_points[loses_against[elve]]
        score += round_points["win"]
  return score

if __name__ == "__main__":
  print(main2())