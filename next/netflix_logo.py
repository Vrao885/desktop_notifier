from turtle import *
t=Turtle()
wn=Screen()
wn.bgcolor("black")
t.shape("turtle")
t.hideturtle()
t.right(90)
pos=[(-40,0),(40,0)]
for x,y in pos:
    t.up()
    t.goto(x,y)
    t.down()
    t.color("red")
    t.begin_fill()


    for i in range(2):  
        t.forward(200)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()
t.up()

t.goto(-40,0)
t.down()
t.left(22)
t.begin_fill()

for i in range(2):
    t.forward(217)  # move forward 217 pixels
    t.left(68)
    t.forward(40)
    t.left(112)

t.end_fill()  # end filling
input()

