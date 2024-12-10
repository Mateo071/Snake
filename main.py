from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

is_game_on = True

screen = Screen()
screen.setup(600, 600, 2500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

while is_game_on:
#   for square in snake_squares:


  screen.update()
  time.sleep(0.1)
  snake.move()

  #Detect collision with food 
  if snake.head.distance(food) < 15:
    food.refresh()
    score.update_score(1)
    snake.grow()

  #Detect collision with wall
  if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
    is_game_on = False
    score.game_over()
    print(f"GG. Your final score was {score.is_score()}. 🏆")

  #Detect collision with tail
  for segment in snake.segments:
    if segment != snake.head:
      if snake.head.distance(segment) < 10:
        is_game_on = False
        score.game_over()
  #If head collides with any segment in the tail:
    #trigger game_over

screen.exitonclick()