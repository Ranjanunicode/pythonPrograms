# python gui program that prints beautiful Indian Flag

# ** FLAG PROJECT **
# Improting and using turtle package
import turtle

def flags():
    # object of turtle module class
    flag = turtle.Turtle()

    # function for blue wheel
  
    # flag outline
    flag.penup()
    flag.setposition(100, 80)
    flag.pendown()
    flag.backward(200)
    flag.right(90)
    flag.forward(50)
    flag.left(90)
    flag.forward(200)
    flag.backward(200)
    flag.right(90)
    flag.forward(50)
    flag.left(90)
    flag.forward(200)
    flag.backward(200)
    flag.right(90)
    flag.forward(50)
    flag.left(90)
    flag.forward(200)
    flag.left(90)
    # green shade lines
    flag.pencolor("green")
    i = 0
    for i in range(17):
        flag.left(5)
        flag.forward(50 + i)
        flag.backward(50+i)
        i = i+1
    flag.right(85)
    # back to top
    flag.pencolor("black")
    flag.forward(150)
    flag.left(90)
    flag.forward(200)
    flag.left(90)
    # orange shade lines
    flag.pencolor("orange")
    i = 0
    for i in range(17):
        flag.left(5)
        flag.forward(50 + i)
        flag.backward(50+i)
        i = i+1
    flag.penup()
    # middle blue wheel
    flag.setposition(0, 0)
    flag.pendown()
    flag.pencolor("blue")
    for i in range(26):
        flag.forward(20)
        flag.backward(20)
        flag.left(14)

    flag.penup()

# flags()
