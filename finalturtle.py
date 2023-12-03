import turtle
from random import randint

turtle.bgcolor("lightblue")

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_text(message, font_size, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.write(message, font=("Arial", font_size, "bold"))

def draw_snowflake(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.shape("turtle")
    turtle.setheading(randint(0, 360))
    for _ in range(6):
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(60)

def draw_globe_with_text():
    turtle.speed(10)

    # Draw the Earth
    draw_circle("blue", 150, 0, 0)

    # Draw continents
    draw_circle("green", 40, -80, 40) 
    draw_circle("green", 40, 80, 40)   
    draw_circle("green", 40, 0, -30)   
    draw_circle("green", 40, -70, -90) 
    draw_circle("green", 40, 80, -90)  
    draw_circle("green", 40, 160, -30) 

    # Write "Merry Christmas" text
    draw_text("Merry Christmas", 20, -60, -200)

    # Draw snowflakes
    for _ in range(20):
        x = randint(-200, 200)
        y = randint(-100, 200)
        draw_snowflake(x, y, 10)

    turtle.hideturtle()
    turtle.done()

# Call the function to draw the globe with text, snowflakes, and sleigh
draw_globe_with_text()
