from turtle import *

screensize(3000,3000)
tracer(0)
m = 10

for i in range(8):
    fd(12*m)
    rt(90)

up()
for x in range(-5,15):
    for y in range(-15,10):
        goto(x*m, y*m)
        dot(4,'red')

update()
done()