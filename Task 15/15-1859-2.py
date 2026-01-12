def f(a):
    for x in range(0,1000):
        for y in range(0,1000):
            F = (2*x + y != 70) or (x < y) or (a < x)
            if not F:
                return False
    return True

for a in range(0,1000):
    if f(a):
        print(a)