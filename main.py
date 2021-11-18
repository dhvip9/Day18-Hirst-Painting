import turtle as t
import colorgram
from random import choice


def rgb_finder(image_path):
    colors = colorgram.extract(image_path, 30)
    rgb_colors_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors_list.append((r, g, b))
    return rgb_colors_list


def color_dots(times, dot_size, space):
    for _ in range(times):
        timmy.dot(dot_size, choice(colours))
        timmy.penup()
        timmy.forward(space)


timmy = t.Turtle()
screen = t.Screen()
screen.colormode(255)
#
colours = rgb_finder("image.jpg")
timmy.speed("fastest")
timmy.penup()
#
a = 325
for _ in range(19):
    timmy.setpos(-340, a)
    timmy.pendown()
    color_dots(20, 15, 35)
    a -= 35

screen.exitonclick()    
