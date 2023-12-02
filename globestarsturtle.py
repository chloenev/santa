import turtle
import random

turtle.bgcolor("lightblue")
turtle.speed(9)

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

def draw_star(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_globe_stars():
    turtle.speed(2)

    # Draw stars in the background
    for _ in range(20):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        size = random.randint(5, 20)
        draw_star(x, y, size)

    # Draw the Earth
    draw_circle("blue", 150, 0, 0)

    # Draw continents
    draw_circle("green", 40, -80, 40)  # North America
    draw_circle("green", 40, 80, 40)   # South America
    draw_circle("green", 40, 0, -30)   # Africa
    draw_circle("green", 40, -70, -90) # Europe
    draw_circle("green", 40, 80, -90)  # Asia
    draw_circle("green", 40, 160, -30) # Australia

    # Write "Merry Christmas" text
    draw_text("Merry Christmas", 20, -60, -200)

    turtle.hideturtle()
    turtle.done()

# Call the function to draw the globe with text and stars
draw_globe_stars()

