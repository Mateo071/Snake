from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
NORTH = 90
WEST = 180
SOUTH = 270
EAST = 0

class Snake:

  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.create_segment(position)

  def move(self):
    """Begins has snake permanently advance"""
    for seg in range(len(self.segments) - 1, 0, -1):
      next_segment_x = self.segments[seg - 1].xcor()
      next_segment_y = self.segments[seg - 1].ycor()
      self.segments[seg].goto(next_segment_x, next_segment_y)
    self.head.forward(MOVE_DISTANCE)

  def create_segment(self, position):
    segment = Turtle("square")
    segment.color("lime")
    segment.up()
    segment.setposition(position)
    self.segments.append(segment)
  
  def grow(self):
    tail_position = self.segments[-1].position()
    position = tail_position
    self.create_segment(position)
  
  def up(self):
    if self.head.heading() != SOUTH:
      self.head.setheading(NORTH)

  def left(self):
    if self.head.heading() != EAST:
      self.head.setheading(WEST)

  def down(self):
    if self.head.heading() != NORTH:
      self.head.setheading(SOUTH)
    
  def right(self):
    if self.head.heading() != WEST:
      self.head.setheading(EAST)