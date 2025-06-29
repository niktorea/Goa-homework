from turtle import *

#we want to paint a house

#step 1: draw a square
width(7)
speed(5)

color("blue")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)    
left(90)

#end of square

#drawing a door
begin_fill()
forward(70)
color("green")
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#the end of roof

#drawing a window

penup()
left(150)
forward(50)

goto(30, 170)
pendown()
color("yellow")
begin_fill
right(300)
right(90)
forward(35)
right(90)
forward(45)
right(90)
forward(35)
right(90)
forward(45)
penup()
goto (135, 170)
pendown()
right(90)
forward(35)
right(90)
forward(45)
right(90)
forward(35)
right(90)
forward(45)
exitonclick()