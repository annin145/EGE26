from turtle import *

screensize(3000,3000)
tracer(0)
m = 20
lt(90)

for i in range(5):
    fd(37 * m)
    rt(90)
    fd(44 * m)
    rt(90)

up()
bk(18 * m)
rt(90)
fd(29 * m)
lt(90)
down()

for i in range(5):
    fd(31 * m)
    rt(90)
    fd(35 * m)
    rt(90)

up()
for x in range(-30,50):
    for y in range(-5,60):
        goto(x *  m, y * m)
        dot(3,"red")

update()
done()

# внутри пересечения фигур 224 точки