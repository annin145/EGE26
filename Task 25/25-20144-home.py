def f(num):
    d = set()
    for i in range(1,int(num**.5)+1):
        if num % i == 0:
            d |= {i,num // i}

    if len(d) >= 2:
        r = max(d) - min(d)
    if r > 1000 and r % 3 == 0:
        return r
    return 0

cnt = 0
for n in range(3_333_338, 10**30):
    if F := f(n):
        print(n, F)
        cnt += 1
        if cnt == 5:
            break