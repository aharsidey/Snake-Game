import turtle
import random
import time

# Creating Turtle Screen

screen = turtle.Screen()
screen.title('Snake Game')
screen.setup(width=700, height=700, starty=10)
screen.tracer(0)
turtle.bgcolor('Black')

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 300)
turtle.pendown()
turtle.color('white')
turtle.forward(600)
turtle.right(90)
turtle.forward(570)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(570)
turtle.right(90)
turtle.hideturtle()

fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
x = random.randint(-290, 270)
y = random.randint(-240, 240)
fruit.goto(x, y)

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('green')
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

scoring = turtle.Turtle()
scoring.speed(0)
scoring.color('white')
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write('Score: ', align='center', font=('Courier', 24, 'bold'))


def snake_up():
    # if snake.direction != 'down':
    snake.direction = 'up'


def snake_down():
    # if snake.direction != 'up':
    snake.direction = 'down'


def snake_left():
    # if snake.direction != 'right':
    snake.direction = 'left'


def snake_right():
    # if snake.direction != 'left':
    snake.direction = 'right'


def snake_move():
    # print(str(snake.direction))
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


screen.listen()
screen.onkeypress(snake_up, "Up")
screen.onkeypress(snake_down, "Down")
screen.onkeypress(snake_left, "Left")
screen.onkeypress(snake_right, "Right")

score = 0
delay = 0.1

old_fruit = []

while True:
    screen.update()

    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)

        fruit.goto(x, y)

        scoring.clear()
        score += 1
        scoring.write('Score:{}'.format(score), align='center', font=('Courier', 24, 'bold'))

        delay -= 0.001

        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('green')
        new_fruit.penup()
        old_fruit.append(new_fruit)

    for i in range(len(old_fruit)-1, 0, -1):
        a = old_fruit[i-1].xcor()
        b = old_fruit[i-1].ycor()
        old_fruit[i].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    snake_move()

    if snake.xcor() >= 290 or snake.xcor() <= -310 or snake.ycor() >= 300 or snake.ycor() <= -270:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('black')
        scoring.goto(0, 0)
        scoring.write(" GAME OVER! YOUR SCORE WAS:{} ".format(score), align='center', font=('Courier', 30, 'bold'))

    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('black')
            scoring.goto(0, 0)
            scoring.write(" GAME OVER! YOUR SCORE WAS:{} ".format(score), align='center', font=('Courier', 30, 'bold'))

    time.sleep(delay)

turtle.Terminator()
