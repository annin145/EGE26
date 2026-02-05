def f(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            d |= {i,num//i}

    if len(d) <7:
        return ()
    return sorted(d)[-7], len(d)

cnt = 0
for n in range(400_000_001,10**10):
    if D := f(n):
        print(*D)
        cnt += 1
        if cnt == 5:
            break