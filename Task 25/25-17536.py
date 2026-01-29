def f(num):
    d = set()
    for i in range(2,int(num ** .5) +1):
        if num % i == 0:
            d |= {i, num // i}

    if len(d) >= 2:
        return max(d) + min(d)
    return 0

cnt = 0
for N in range(800_001, 10**30):
    F = f(N)
    if F % 10 == 4:
        print(N, F)
        cnt += 1
        if cnt == 5:
            break