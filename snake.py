from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

  def __init__(self):
    self.segments = []
    self.create_snake()

  def create_snake(self):
    for position in STARTING_POSITIONS:
      segment = Turtle("square")
      segment.color("white")
      segment.up()
      segment.setposition(position)
      self.segments.append(segment)
      segment.speed("slowest")

  def move(self):
    """Begins has snake permanently advance"""
    for seg in range(len(self.segments) - 1, 0, -1):
      next_segment_x = self.segments[seg - 1].xcor()
      next_segment_y = self.segments[seg - 1].ycor()
      self.segments[seg].goto(next_segment_x, next_segment_y)
    self.segments[0].forward(MOVE_DISTANCE)