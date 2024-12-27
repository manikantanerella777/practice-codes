from sketchpy import canvas
import turtle
obj = canvas.sketch_from_svg("PathToImage.svg")
t = turtle.Turtle()
t.penup()

t.pendown()
obj.draw()