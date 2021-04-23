import copy
import random
# Consider using the modules imported above.

class Hat():
  def __init__(self, **ballsDict):
    self.ballsList = ballsDict
    self.contents = []
    [[self.contents.append(k) for i in range(v)] for (k,v) in ballsDict.items()]

  def __str__(self):
    return str(self.contents)
    
  def draw(self, balls_to_draw):
    drawnBalls = []
    while balls_to_draw != 0:
      if balls_to_draw > len(self.contents):
        self.contents += drawnBalls
      else:
        drawnBalls.append(self.contents.pop( random.randint(0,len(self.contents)-1) ))
    
      balls_to_draw -= 1
    return drawnBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  matchCount, expCount = 0, 0
  while expCount < num_experiments:
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)
    drawn_balls = {}
    for color in drawn:
      if drawn_balls.get(color) == None:
        drawn_balls[color] = 1
        continue
      drawn_balls[color] += 1
    
    match = True
    for k,v in expected_balls.items():
      if drawn_balls.get(k) == None or drawn_balls[k] < v:
        match = False
        break
    if match: matchCount += 1

    expCount += 1

  probability = matchCount/num_experiments
  return probability