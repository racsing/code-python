# Downloaded Required colorgram.py 1.2.0 pkg
# pip3 install colorgram.py


# Extract color from image
#

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# Create a painting
import random
import turtle as turtle

turtle.colormode(255)
tim = turtle.Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (223, 137, 176), (143, 108, 57),
              (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227),
              (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36),
              (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190),
              (87, 46, 33), (37, 45, 83)]

tim.setheading(215)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
