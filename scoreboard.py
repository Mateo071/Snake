from turtle import Turtle
STARTING_SCORE = 0
ALIGNMENT ="center"
SCORE_FONT = ("arial", 12, "bold")
END_FONT = ("arial", 24, "bold")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("white")
    self.up()
    self.goto(0, 280)
    self.score = STARTING_SCORE
    self.update_score(STARTING_SCORE)
    
  def update_score(self, new_points):
    self.clear()
    self.score += new_points
    self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", move=False, align=ALIGNMENT, font=END_FONT)

  def is_score(self):
    return self.score