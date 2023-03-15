import turtle

t = turtle

wn = turtle.Screen()
wn.title("Ping-Pong")
wn.bgcolor("grey")
wn.setup(width=1200, height=900)
wn.tracer(0)

leftp = t.Turtle()
leftp.speed(0)
leftp.shape("square")
leftp.color("green")
leftp.shapesize(stretch_wid=5, stretch_len=1)
leftp.penup()
leftp.goto(-575, 0)

rightp = t.Turtle()
rightp.speed(0)
rightp.shape("square")
rightp.color("green")
rightp.shapesize(stretch_wid=5, stretch_len=1)
rightp.penup()
rightp.goto(570, 0)

ball = t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

def leftp_up():
    y = leftp.ycor()
    y += 20
    leftp.sety(y)

def leftp_down():
    y = leftp.ycor()
    y -= 20
    leftp.sety(y)

def rightp_up():
    y = rightp.ycor()
    y += 20
    rightp.sety(y)

def rightp_down():
    y = rightp.ycor()
    y -= 20
    rightp.sety(y)

wn.listen()
wn.onkeypress(leftp_up, "w")
wn.onkeypress(leftp_down, "s")
wn.onkeypress(rightp_up, "Up")
wn.onkeypress(rightp_down, "Down")

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 440:
        ball.sety(440)
        ball.dy *= -1

    if ball.ycor() < -440:
        ball.sety(-440)
        ball.dy *= -1

    if ball.xcor() > 590:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -590:
        ball.goto(0, 0)
        ball.dx *= -1

    if (ball.xcor() > 550 and ball.xcor() < 560) and (ball.ycor() < rightp.ycor() + 50 and ball.ycor() > rightp.ycor() - 50):
        ball.setx(550)
        ball.dx *= -1

    if (ball.xcor() < -550 and ball.xcor() > -560) and (ball.ycor() < leftp.ycor() + 50 and ball.ycor() > leftp.ycor() - 50):
        ball.setx(-550)
        ball.dx *= -1