from turtle import *

screensize(3000, 3000)
tracer(0)
m = 10

for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
fd(1* m)
rt(90)
fd(5 * m)
lt(90)
down()

for i in range(9):
    fd(53* m)
    rt(90)
    fd(75* m)
    rt(90)

up()

for x in range(-35,25):
    for y in range(-10,80):
        goto(x * m, y * m)
        dot(3,"red")

update()
done()