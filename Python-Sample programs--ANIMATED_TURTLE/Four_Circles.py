from turtle import *
speed(7)
pensize(5)
pencolor('blue')

up()
goto(-200,200)
down()

begin_fill()
fillcolor('green')
circle(120)
end_fill()

up()
home()
goto(200,-200)
down()

begin_fill()
fillcolor('yellow')
circle(120)
end_fill()

up()
home()
goto(200,200)
down()

begin_fill()
fillcolor('pink')
circle(120)
end_fill()

up()
home()
goto(-200,-200)
down()

begin_fill()
fillcolor('red')
circle(120)
end_fill()

hideturtle()
done()