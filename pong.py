#Pong in Python 3
# Part1 Getting started

import turtle

win = turtle.Screen()
win.title("Pong by NikkiLinx")
win.bgcolor("black")
win.setup(width = 800, height = 600)  #size of the window that opens
win.tracer(0)

#score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  #set to max possible speed
paddle_a.shape("square")  #default is 20pxl x 20pxl
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)  #size of paddle
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  #set to max possible speed
paddle_b.shape("square")  #default is 20pxl x 20pxl
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)  #size of paddle
paddle_b.penup()
paddle_b.goto(+350,0)

#Ball

ball = turtle.Turtle()
ball.speed(0)  #set to max possible speed
ball.shape("circle")  #default is 20pxl x 20pxl
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .15 #delta change
ball.dy = -.15

# Pen (Scoring mechanism)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #don't want to draw a line when it moves
pen.hideturtle()  #don't want to see
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align = "center", font=("Courier", 20, "bold"))



#Functions

def paddle_a_up(): 
    y = paddle_a.ycor()  #returns y coordinates, assign to y
    y += 20
    paddle_a.sety(y)

def paddle_a_down(): 
    y = paddle_a.ycor()  #returns y coordinates, assign to y
    y -= 20
    paddle_a.sety(y)

    
def paddle_b_up(): 
    y = paddle_b.ycor()  #returns y coordinates, assign to y
    y += 20
    paddle_b.sety(y)

def paddle_b_down(): 
    y = paddle_b.ycor()  #returns y coordinates, assign to y
    y -= 20
    paddle_b.sety(y)

# Keyboard binding

win.listen()  #listen for keyboard input
win.onkeypress(paddle_a_up, "w")  #when keyboard presses w, call function paddle_a_up
win.onkeypress(paddle_a_down, "s")  #when keyboard presses s, call function paddle_a_down
win.onkeypress(paddle_b_up, "Up")  #when keyboard presses up arrow, call function paddle_b_up
win.onkeypress(paddle_b_down, "Down")  #when keyboard presses down, call function paddle_b_down






#Main Game loop
while True:
    win.update()  #everytime loop runs, window updates

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1 #reverses the direction of the ball

    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1 #reverses the direction of the ball

    if ball.xcor() > 390: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 20, "bold"))
    
    if ball.xcor() < -390: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 20, "bold"))

    # Paddle and ball collisions

    if ball.xcor() > 330 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40): #edges are touching, and it's within the top and bottom of paddle 
        ball.setx(330)
        ball.dx *= -1

    if ball.xcor() < -330 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40): #edges are touching, and it's within the top and bottom of paddle 
        ball.setx(-330)
        ball.dx *= -1
