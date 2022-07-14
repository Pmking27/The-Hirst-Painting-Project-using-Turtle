from turtle import Turtle,Screen,colormode,hideturtle
import random

color_list=[(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229),
(223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91),
(238, 89, 49),(142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), 
(4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221),(29, 90, 95),
(233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83),(245, 205, 7), (35, 88, 88), (103, 24, 56)]

timmy = Turtle()
timmy.hideturtle()
timmy.speed(0)
colormode(255)

timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

def hirst_painting(size, distance):
    for i in range(size):
        
        for j in range(size):
            timmy.penup()
            timmy.forward(distance)
            timmy.pendown()
            timmy.dot(20,random.choice(color_list))
        timmy.penup()    
        timmy.left(90)
        timmy.forward(distance)
        timmy.left(90)
        timmy.forward(distance*size)
        timmy.left(180)

hirst_painting(7,50)

screen = Screen()
screen.exitonclick()