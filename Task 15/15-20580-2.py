def f(a):
    for x in range(1,1000):
        for y in range(1,1000):
            F = (9*x + y > a) or (x >= 36) or (y >= 18)
            if not F:
                return False
    return True

for a in range(0,1000):
    if f(a):
        print(a)