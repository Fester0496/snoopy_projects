import turtle


# game window creation
win = turtle.Screen()
win.title("SNAKE GAME")
win.bgcolor("Black")
win.setup(width=600, height=600)
win.register_shape("Sprite-0001.gif")

# Snake head creation
head = turtle.Turtle()
head.speed(1)
head.shape("circle")
head.color("red")
head.goto(0, 0)
head.penup()
head.direction = "stop"



# Food creation
food = turtle.Turtle()
food.speed(0)
food.goto(0, 100)
food.shape("Sprite-0001.gif")
food.penup()


# Head controlls
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def stop():
    head.direction = "stop"

# Direction controll
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "stop":
        y = head.ycor()
        x = head.xcor()
        head.sety(y = y)
        head.setx(x = x)
    

# Map controlls
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_right, "Right")
win.onkey(go_left, "Left")
win.onkey(stop, "space")






while True:
    win.update()
    move()
