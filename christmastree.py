import turtle
from random import randint
# 4 tuples
position_tree = ((50, 20), (80, 0), (130, -40), (180, -70))

window = turtle.Screen()
window.bgcolor("sky blue")

tree = turtle.Turtle()
tree.penup()
tree.color("forest green")

stem = turtle.Turtle()
stem.color("brown")
stem.right(90)
stem.pensize(50)
stem.penup()
stem.forward(100)
stem.pendown()
stem.forward(300)



def make_tree(size, position):
    tree.begin_fill()
    tree.setposition(0, position)
    tree.setposition(size, position-size)
    tree.setposition(-size, position-size)
    tree.setposition(0, position)
    tree.end_fill()

def make_star():
    turns = 5
    turtle.begin_fill()
    while turns > 0:
        turtle.forward(25)
        turtle.left(145)
        turns = turns - 1
    turtle.end_fill()

for size, position in position_tree:
    make_tree(size, position)

number_stars = 0
while number_stars < 50:
    x = randint (-300,300)
    y = randint (-30,300)
make_star()
turtle.color("yellow")
turtle.penup()
turtle.goto(x,y)
number_stars = number_stars + 1

turtle.done()
