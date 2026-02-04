def f(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
                d |= {i,num//i}

    if len(d) > 1:
        m = max(d) + min(d)
        if m % 10 == 4:
            return m
    return 0

cnt = 0
for n in range(800_000, 10**30):
    if F := f(n):
        cnt += 1
        print(n, F)
        if cnt == 5:
            break