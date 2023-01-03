import turtle # here we imported turtle

t = turtle.Turtle() # define our turtle
turtle.Screen().bgcolor('black') # set background color to black

t.right(90) # turn turtle to face up by (90)

pos = [(-40,0),(40,0)] # define our positions cords
for x,y in pos: # for each position
    t.up() # lift pen
    t.goto(x,y) # move to position
    t.down() # put pen down
    t.color('red') # set color to red
   
    for i in range(2): # for each side
        t.forward(200) # move forward 200 pixels
        t.left(90) # turn left 90 degrees