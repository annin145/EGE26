def f(x,y):
    b = 50 <= x <= 70
    return (2*x + y != 150) or (not b) or (a >y)

for a in range(1,1000):
    if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        break