from turtle import *

screensize(3000,3000)
tracer(0)
m = 15

for i in range(2):
    fd(1*m)
    lt(270)
    fd(16*m)
    rt(90)

up()
bk(4*m)
rt(90)
fd(10*m)
lt(90)
down()

for i in range(2):
    fd(17*m)
    rt(90)
    fd(7*m)
    rt(90)

up()
for x in range(-10,15):
    for y in range(-25,3):
        goto(x*m,y*m)
        dot(3, 'red')

update()
done()
