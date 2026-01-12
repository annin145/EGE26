def f(a):
    for x in range(0,1000):
        for y in range(0,1000):
            F = (x < a) or (y < a) or (x + 2*y > 50)
            if not F:
                return False
    return True

for a in range(0,1000):
    if f(a):
        print(a)