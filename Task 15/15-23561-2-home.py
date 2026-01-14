def f(a):
    for x in range(0,1000):
        F = (x % 128 == 0) <= ((x % a != 0) <= (x % 80 != 0))
        if not F:
            return False
    return True

for a in range(1,1000):
    if f(a):
        print(a)