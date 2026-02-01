def f(num):
    d = set()
    for i in range(2,int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num //i}

    for i in sorted(d):
        if i != 7 and i % 10 == 7:
            return i
    return 0

cnt = 0
for N in range(700_001, 10**20):
    F = f(N)
    if F:
        print(N,F)
        cnt += 1
        if cnt == 5:
            break