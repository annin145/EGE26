def f(a):
    for x in range(0,1000):
        for y in range(0,1000):
            F = ((x + y) <= 30) or (y <= (x +2)) or (y >= a)
            if not F:
                return False
    return True

for a in range(0,1000):
    if f(a):
        print(a)

#17