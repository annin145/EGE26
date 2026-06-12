def f(x):
    return ((x&52 != 0) and (x&48 == 0)) <= (not(x&a == 0))

for a in range(1,1000):
    if all(f(x) for x in range(1,1000)):
        print(a)
        break