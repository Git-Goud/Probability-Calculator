import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.contents += v * [k]
    print(self.contents)

  def draw(self, num):
    try:
      balls = random.sample(self.contents, num) #Remove balls at random from contents
    except:
      balls = copy.deepcopy(self.contents)

    for ball in balls:
        self.contents.remove(ball) #balls should not go back into the hat during the draw
    
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    hat1 = copy.deepcopy(hat)
    balls = hat1.draw(num_balls_drawn)

    expected_balls_list = []

    for k, v in expected_balls.items():
      expected_balls_list += v * [k]

    if contains (expected_balls_list, balls):
      M += 1

  probability = M / num_experiments #get probability
  return probability

def contains (exptected_balls, actual_balls):
  for b in exptected_balls:
    if b in actual_balls:
      actual_balls.remove(b)
    else:
      return False
  return True
