import turtle

turtle.pensize(1)

for i in range(0, 700, 2):
    turtle.forward(i)
    turtle.right(90)

turtle.Screen().exitonclick()