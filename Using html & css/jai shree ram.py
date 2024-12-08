from turtle import *
title('jai shree ram')
bgcolor("black")
pensize(5)
pencolor('orange')
speed(2)

mani=['JAI SHREE RAM','JAI SHREE RAM','JAI SHREE RAM',
'JAI SHREE RAM','JAI SHREE RAM','JAI SHREE RAM',
'JAI SHREE RAM','JAI SHREE RAM','JAI SHREE RAM',
'JAI SHREE RAM','JAI SHREE RAM','JAI SHREE RAM',
'JAI SHREE RAM','JAI SHREE RAM','JAI SHREE RAM',
'JAI SHREE RAM','JAI SHREE RAM','JAI SHREE RAM',
'JAI SHREE RAM','JAI SHREE RAM','JAI SHREE RAM',
'JAI SHREE RAM','JAI SHREE RAM','JAI SHREE RAM',
'JAI SHREE RAM','JAI SHREE RAM','JAI SHREE RAM',
'JAI SHREE RAM','JAI SHREE RAM','JAI SHREE RAM']

angle=360/49
penup()
sety(-1)
for i in range(50):
    lt(angle)
    fd(260)
    write(mani[i],align='right',bd(260))

penup()
goto(-40,-20)
pendown()
done()