from turtle import *

tracer(0)
screensize(3000,3000)
m = 10

for i in range(2):
    fd(6*m)
    lt(270)
    bk(20*m)
    rt(90)

up()
fd(3*m)
rt(90)
bk(3*m)
lt(90)

down()
for i in range(2):
    fd(15*m)
    rt(90)
    fd(70*m)
    rt(90)

up()
for x in range(-10,10):
    for y in range(-10,10):
        goto(x*m,y*m)
        dot(3, 'red')

update()
done()