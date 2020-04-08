import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("red")
wn.title("snake game")

class Game(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="left", font=("Arial",14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

class Border(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-250, -250)
        self.pendown()
        self.goto(-250, 250)
        self.goto(250, 250)
        self.goto(250, -250)
        self.goto(-250, -250)

class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("triangle")
        self.color("white")
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 240 or self.xcor() < -240:
            self.left(60)
        if self.ycor() > 240 or self.ycor() < -240:
            self.left(60)

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.speed += 1

class Goal(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("circle")
        self.speed = 1
        self.goto(random.randint(-220,220), random.randint(-220,220))
        self.setheading(random.randint(0,360))

    def jump(self):
        self.goto(random.randint(-220, 220), random.randint(-220, 220))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 240 or self.xcor() < -240:
             self.left(60)
        if self.ycor() > 240 or self.ycor() < -240:
             self.left(60)

def isCollision(t1, t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))

    if distance < 20:
        return True
    else:
        return False 

player = Player()
border = Border()
game = Game()


border.draw_border()

goals = []
for count in range(6):
    goals.append(Goal())

turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.increasespeed, "Up")

wn.tracer(0)

while True:
    wn.update()
    player.move()

    for goal in goals:
        goal.move()
    

    if isCollision(player, goal):
        goal.jump()
        game.change_score(10)


