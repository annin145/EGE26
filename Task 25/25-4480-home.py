def f(num):
    d = set()
    for i in range(1,int(num**.5)+1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 10:
        y = 1
        for i in d:
            y *= i
        if sum(d) % 2 != 0 and y % 2 != 0:
            return len(d)
    return 0

cnt = 0
for n in range(800_001, 10**30):
    if F := f(n):
        print(n, F)
        cnt += 1
        if cnt == 6:
            break