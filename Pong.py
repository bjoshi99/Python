#Game logic

import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Variables
scoreA = 0
scoreB = 0
colision = 0

#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = 0.25

#Lable for points and time
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA: {} PlayerB: {}".format(scoreA, scoreB), align="center", font=("Courier",24,"normal"))

#Function

def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

#key Board binding
wn.listen()
#For paddle_a
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
#for paddle_b
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Loop for game
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking - check y axis
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        colision += colision
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        colision += 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)       

    if ball.xcor() > 390:
        ball.goto(0,0)
        colision = 0
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("PlayerA: {} PlayerB: {}".format(scoreA, scoreB), align="center", font=("Courier",24,"normal"))

    elif ball.xcor() < -390:
        ball.goto(0,0)
        colision = 0
        ball.dx *= -1
        scoreB += 1
        pen.clear()             
        pen.write("PlayerA: {} PlayerB: {}".format(scoreA, scoreB), align="center", font=("Courier",24,"normal"))

    #Paddle logic
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if colision > 20:
        ball.dx *= 2
        ball.dy *= 2
        colision = 0