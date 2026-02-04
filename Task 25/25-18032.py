def f(num):
    s = 0
    for i in range(1,n+1):
        if num % i == 0:
            s += i
    return s

for n in range(1_000,10_000):
    s = f(n)
    if s % 100 == 23:
        print(n,s)