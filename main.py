import turtle as turtle_module
import random

turtle_module.colormode(255)
dots=turtle_module.Turtle()
# import colorgram
#
#
# colors = colorgram.extract('hirst_img.jpg',30)
#
# # print(colors)
# rgb_colors = []
# for i in range(29):
#     color = colors[i]
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

colors = [(196, 166, 105), (133, 167, 194), (46, 103, 147), (147, 89, 40), (9, 21, 54), (189, 156, 33), (225, 208, 112), (62, 22, 9), (68, 120, 77), (58, 12, 23), (185, 140, 166), (136, 181, 149), (136, 28, 12), (132, 76, 105), (14, 43, 26), (18, 53, 137), (121, 26, 41), (170, 101, 137), (92, 152, 97), (175, 189, 217), (86, 121, 184), (22, 93, 65), (67, 153, 170), (184, 99, 86), (210, 177, 204)]
dots.hideturtle()
dots.penup()
dots.speed("fastest")
dots.setx(-250)
dots.sety(-250)

number_of_dots = 101

for dot_count in range(1, number_of_dots):
    dots.dot(10,random.choice(colors))
    dots.forward(50)
    if dot_count % 10 == 0:
        dots.setheading(90)
        dots.forward(50)
        dots.setheading(180)
        dots.forward(500)
        dots.setheading(0)






screen=turtle_module.Screen()
screen.exitonclick()

