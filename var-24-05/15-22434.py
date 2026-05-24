def f(x,y):
    return (x**2 <= 136) or (y < 4*x + a - 70) or (2*y > 51)

for a in range(1,1000):
    if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        break