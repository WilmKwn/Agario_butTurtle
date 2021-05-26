import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor("lightblue")

player = turtle.Turtle()
player.penup()
player.color("orange")
player.shape("turtle")
player.turtlesize(stretch_wid=2.5, stretch_len=2.5, outline=None)

player2 = turtle.Turtle()
player2.penup()
player2.color("blue")
player2.shape("turtle")
player2.turtlesize(stretch_wid=2.5, stretch_len=2.5, outline=None)

player3 = turtle.Turtle()
player3.penup()
player3.color("yellow")
player3.shape("turtle")
player3.turtlesize(stretch_wid=2.5, stretch_len=2.5, outline=None)

stretch_wid=2.5
stretch_len=2.5
speed = 1

def left():
    player.left(30)

def right():
    player.right(30)

def right2():
    player2.right(30)

def left2():
    player2.left(30)

def right3():
    player3.right(30)

def left3():
    player3.left(30)

screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(left2, "z")
screen.onkey(right2, "x")
screen.onkey(left3, "n")
screen.onkey(right3, "m")
screen.listen()
    
ball = turtle.Turtle()
ball.penup()
ball.color("black")
ball.shape("circle")
ball.setposition(random.randint(-950,950),random.randint(-500,500))

ball3 = turtle.Turtle()
ball3.penup()
ball3.color("black")
ball3.shape("circle")
ball3.setposition(random.randint(-950,950),random.randint(-500,500))

ball4 = turtle.Turtle()
ball4.penup()
ball4.color("black")
ball4.shape("circle")
ball4.setposition(random.randint(-950,950),random.randint(-500,500))

ball5 = turtle.Turtle()
ball5.penup()
ball5.color("black")
ball5.shape("circle")
ball5.setposition(random.randint(-950,950),random.randint(-500,500))

ball2 = turtle.Turtle()
ball2.penup()
ball2.color("black")
ball2.shape("circle")
ball2.setposition(random.randint(-950,950),random.randint(-500,500))

while True:
    player.forward(3)
    player2.forward(3)
    player3.forward(3)

    if player.xcor() > 950 or player.xcor() < -950:
        player.left(180)

    if player2.xcor() > 950 or player2.xcor() < -950:
        player2.left(180)

    if player.ycor() > 500 or player.ycor() < -500:
        player.left(180)

    if player2.ycor() > 500 or player2.ycor() < -500:
        player2.left(180)

    if player3.xcor() > 950 or player3.xcor() < -950:
        player3.left(180)

    if player3.ycor() > 500 or player3.ycor() < -500:
        player3.left(180)


    d = math.sqrt(math.pow(player.xcor()-ball.xcor(),2) + math.pow(player.ycor()-ball.ycor(),2))
    if d < 20:
        ball.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player2.xcor()-ball.xcor(),2) + math.pow(player2.ycor()-ball.ycor(),2))
    if d < 20:
        ball.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player2.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player3.xcor()-ball.xcor(),2) + math.pow(player3.ycor()-ball.ycor(),2))
    if d < 20:
        ball.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player3.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player.xcor()-ball2.xcor(),2) + math.pow(player.ycor()-ball2.ycor(),2))
    if d < 20:
        ball2.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid - 1
        stretch_len = stretch_len - 1
        player.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player2.xcor()-ball2.xcor(),2) + math.pow(player2.ycor()-ball2.ycor(),2))
    if d < 20:
        ball2.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid - 1
        stretch_len = stretch_len - 1
        player2.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player3.xcor()-ball2.xcor(),2) + math.pow(player3.ycor()-ball2.ycor(),2))
    if d < 20:
        ball2.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid - 1
        stretch_len = stretch_len - 1
        player3.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player.xcor()-ball3.xcor(),2) + math.pow(player.ycor()-ball3.ycor(),2))
    if d < 20:
        ball3.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player2.xcor()-ball3.xcor(),2) + math.pow(player2.ycor()-ball3.ycor(),2))
    if d < 20:
        ball3.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player2.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player3.xcor()-ball3.xcor(),2) + math.pow(player3.ycor()-ball3.ycor(),2))
    if d < 20:
        ball3.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player3.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player.xcor()-ball4.xcor(),2) + math.pow(player.ycor()-ball4.ycor(),2))
    if d < 20:
        ball4.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player2.xcor()-ball4.xcor(),2) + math.pow(player2.ycor()-ball4.ycor(),2))
    if d < 20:
        ball4.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player2.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player3.xcor()-ball4.xcor(),2) + math.pow(player3.ycor()-ball4.ycor(),2))
    if d < 20:
        ball4.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player3.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player.xcor()-ball5.xcor(),2) + math.pow(player.ycor()-ball5.ycor(),2))
    if d < 20:
        ball5.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player2.xcor()-ball5.xcor(),2) + math.pow(player2.ycor()-ball5.ycor(),2))
    if d < 20:
        ball5.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player2.turtlesize(stretch_wid, stretch_len)

    d = math.sqrt(math.pow(player3.xcor()-ball5.xcor(),2) + math.pow(player3.ycor()-ball5.ycor(),2))
    if d < 20:
        ball5.setposition(random.randint(-950,950), random.randint(-500,500))
        stretch_wid = stretch_wid + 1
        stretch_len = stretch_len + 1
        player3.turtlesize(stretch_wid, stretch_len)

        

        

    d = math.sqrt(math.pow(player.xcor()-player2.xcor(),2) + math.pow(player.ycor()-player2.ycor(),2))
    if d < 30 and player.turtlesize() > player2.turtlesize():
        player2.hideturtle()

    d = math.sqrt(math.pow(player.xcor()-player2.xcor(),2) + math.pow(player.ycor()-player2.ycor(),2))
    if d < 30 and player.turtlesize() < player2.turtlesize():
        player.hideturtle()

    d = math.sqrt(math.pow(player3.xcor()-player2.xcor(),2) + math.pow(player3.ycor()-player2.ycor(),2))
    if d < 30 and player3.turtlesize() > player2.turtlesize():
        player2.hideturtle()

    d = math.sqrt(math.pow(player3.xcor()-player2.xcor(),2) + math.pow(player3.ycor()-player2.ycor(),2))
    if d < 30 and player3.turtlesize() < player2.turtlesize():
        player3.hideturtle()

    d = math.sqrt(math.pow(player.xcor()-player3.xcor(),2) + math.pow(player.ycor()-player3.ycor(),2))
    if d < 30 and player.turtlesize() > player3.turtlesize():
        player3.hideturtle()

    d = math.sqrt(math.pow(player.xcor()-player3.xcor(),2) + math.pow(player.ycor()-player3.ycor(),2))
    if d < 30 and player.turtlesize() < player3.turtlesize():
        player.hideturtle()
