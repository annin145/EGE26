def f(x):
    b = 50 <= x <= 70
    return (x % a == 0) or (b <= (x % 16 != 0))

for a in range(1,1000)[::-1]:
    if all(f(x) for x in range(1,1000)):
        print(a)
        break