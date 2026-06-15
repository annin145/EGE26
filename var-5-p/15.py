def f(x):
    c = 30 <= x <= 45
    return ((x % a == 0) and c) <= (not(x%12==0))

for a in range(1,1000):
    if all(f(x) for x in range(1,1000)):
        print(a)
        break


