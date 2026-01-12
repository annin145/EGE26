def f(a):
    for x in range(0,1000):
        for y in range(0,1000):
            F = (x + 2*y > a) or (y < x) or (x < 30)
            if not F:
                return False
    return True

for a in range(0,1000):
    if f(a):
        print(a)