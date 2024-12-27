import turtle
import colorsys
t=turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')
h=0
for i in range(360):
	c=colorsys.hsv_to_rgb(h,1,0.8)
	t.color(c)
	t.goto(1,1)
	t.fd(150+i/5)
	t.right(90)
	t.fd(150+i/4)
	
	t.rt(91)
	h +=0.004
	
t.done(0)