from turtle import *

screensize(3000,3000)
tracer(0) # отключение анимации
m = 15 # масштаб

for i in range(2):
    forward(10 * m)
    right(90)
    forward(18 * m)
    right(90)

up()

fd(5 * m)
rt(90)
fd(7 * m)
lt(90)

down()

for i in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
for x in range(-3, 20):
    for y in range(-20, 10):
        goto(x * m,y * m)
        dot(5,'green')

update()
done()
