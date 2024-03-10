import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
"Move Snake"
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    # detect collision from the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

    #Detect collition with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on= False
        score.game_over()

    #detect collition with tail using slice
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            score.game_over()



screen.exitonclick()
