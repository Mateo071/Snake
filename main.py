from turtle import Turtle, Screen
from snake import Snake
import random
import time

#score = 0
#snake_length = score + 3
#origin_x = 0
#origin_y = 0
is_game_on = True
# starting_positions = []

screen = Screen()
screen.setup(600, 600, 2500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

def move_right():
  pass

# for n in range(snake_length):
#   snake = Turtle("square")
#   snake.color("white")
#   snake.up()
#   snake.setposition(origin_x, origin_y)
#   snake_squares.append(snake)
#   snake.speed("slowest")
#   starting_positions.append((origin_x, origin_y))
#   origin_x -= 20
  

def up():
  print("looking up")
  snake_head = snake_squares[0]
  snake_head.setheading(90)

screen.onkey(up, "Up")
while is_game_on:
#   for square in snake_squares:

#     if square.xcor() > 260 or square.xcor() < -260 or square.ycor() > 260 or square.ycor() < -260 :
#       is_game_on = False
#       print("gg")

  snake.move() 
  screen.update()
  time.sleep(0.1)
  # for square in range(len(snake_squares) - 1, 0, -1):
  #   next_square_x = snake_squares[square - 1].xcor()
  #   next_square_y = snake_squares[square - 1].ycor()
  #   snake_squares[square].goto(next_square_x, next_square_y)
  # snake_squares[0].forward(20)


screen.exitonclick()