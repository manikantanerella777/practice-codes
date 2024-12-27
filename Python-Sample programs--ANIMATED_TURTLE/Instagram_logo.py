from turtle import *
#turtle.bgcolor('black')
pencolor('blue')
pensize(5)
speed(6)
bgcolor('yellow')
up()
goto(-100,100)
down()

begin_fill()
fillcolor('pink')
for i in range(4):
	fd(200)
	rt(90)
end_fill()

up()
goto(0,0)
down()

up()
goto(-0,-50)
down()
circle(40)

up()
goto(60,60)
down()

circle(10)

up()
goto(-200,-200)
fd(100)
down()
pencolor('red')
write('INSTAGRAM')

up()
goto(-500,-500)
fd(650)
down()
write('Art by mani')
hideturtle()
done()