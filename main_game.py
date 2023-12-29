import turtle
import random
import time

# turtle screen
screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width=1280, height=720)
screen.tracer(0)
turtle.bgcolor('chartreuse3')

# border for looks
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# score
score = 0
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('blue')
fruit.penup()
fruit.goto(30, 30)

# bad food
bad_fruit = turtle.Turtle()
bad_fruit.speed(0)
bad_fruit.shape('circle')
bad_fruit.color('crimson')
bad_fruit.penup()
bad_fruit.goto(-30, -30)

old_fruit = []

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score :", align="center", font=("Courier", 24, "bold"))

# movement
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    elif snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    elif snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkey(snake_go_up, "w")
screen.onkey(snake_go_down, "s")
screen.onkey(snake_go_left, "a")
screen.onkey(snake_go_right, "d")


# Main game loop
while True:
    screen.update()

    # Check for a collision with the border
    if (
        snake.xcor() > 280
        or snake.xcor() < -300
        or snake.ycor() > 240
        or snake.ycor() < -240
    ):
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0,0)
        scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
        time.sleep(2)
        screen.bye()

    # Check for a collision with the fruit
    if (
        snake.xcor() > fruit.xcor() - 15
        and snake.xcor() < fruit.xcor() + 15
        and snake.ycor() > fruit.ycor() - 15
        and snake.ycor() < fruit.ycor() + 15
    ):
        # Increase the score
        score += 10

        # Move the fruit to a random position within the borders
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)

        # Move the bad_fruit to a random position within the borders
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        bad_fruit.goto(x, y)

        # Add the fruit to the old_fruit list
        old_fruit.append(turtle.Turtle())
        old_fruit[-1].speed(0)
        old_fruit[-1].shape("square")
        old_fruit[-1].color("grey")
        old_fruit[-1].penup()
        old_fruit[-1].goto(0, 0)

        # Update the score display
        scoring.clear()
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

    # Check for a collision with the bad_fruit
    if (
        snake.xcor() > bad_fruit.xcor() - 15
        and snake.xcor() < bad_fruit.xcor() + 15
        and snake.ycor() > bad_fruit.ycor() - 15
        and snake.ycor() < bad_fruit.ycor() + 15
    ):
        # Decrease the length of the snake
        if len(old_fruit) > 0:
            old_fruit[-1].goto(1000, 1000)
            old_fruit.pop()

        # Move the bad_fruit to a random position within the borders
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        bad_fruit.goto(x, y)

        # Update the score display
        score -= 10
        scoring.clear()
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

        # Check if the score is below zero and end the game
        if score < 0:
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0,0)
            scoring.write("    GAME OVER \n You Died Of Poison",align="center",font=("Courier",30,"bold"))
            time.sleep(2)
            screen.bye()

    # Move the snake
    for index in range(len(old_fruit) - 1, 0, -1):
        x = old_fruit[index - 1].xcor()
        y = old_fruit[index - 1].ycor()
        old_fruit[index].goto(x, y)

    if len(old_fruit) > 0:
        x = snake.xcor()
        y = snake.ycor()
        old_fruit[0].goto(x, y)

    snake_move()

    # Delay
    time.sleep(delay)

# Display main window
turtle.mainloop()
