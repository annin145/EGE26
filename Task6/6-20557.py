from turtle import *

screensize(3000,3000)
tracer(0)
m = 10

for i in range(4):
    fd(36*m)
    rt(90)
    fd(41*m)
    rt(90)

up()
rt(90)
fd(20*m)
lt(90)
fd(20*m)

down()

for i in range(4):
    fd(25*m)
    rt(90)

up()
fd(7*m)
lt(90)
fd(7*m)
rt(90)

down()

for i in range(7):
    fd(16*m)
    rt(90)

up()
for x in range(20,):
    for y in range(-30,3):
        goto(x*m,y*m)
        dot(5,'red')

update()
done()