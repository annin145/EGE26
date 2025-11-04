from turtle import *

screensize(3000,3000)
tracer(0)
m = 20
lt(90)

c = 30 # ответ на вопрос задачи
for i in range(4):
    fd(c * m)
    rt(90)
    fd(48 * m)
    rt(90)

up()
fd(27 * m)
rt(90)
fd(24 * m)
lt(90)
down()

for i in range(4):
    fd(29 * m)
    rt(90)
    bk(18 * m)
    rt(90)

up()
for x in range(-5,50):
    for y in range(-5,70):
        goto(x * m, y * m)
        dot(3,"red")

update()
done()