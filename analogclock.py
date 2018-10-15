# Analog Clock

import time
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Analog Clock")
wn.tracer(0)

# Create our drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

def draw_clock(h, m, s, pen):

    # Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color('white')
    pen.pendown()
    pen.circle(210)

    # Draw the hour markers
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for i in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(5)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)


    # Draw the hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color('white')
    pen.setheading(90)
    angle = (h /12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(130)

    # Draw the minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('white')
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(200)

    # Draw the second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('red')
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(200)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(h, m, s, pen)
    wn.update()
    time.sleep(1)

    pen.clear()




wn.mainloop()