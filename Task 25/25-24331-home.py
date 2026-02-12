def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i < int(num**.5)+1:
        while num % i == 0:
            d += [i]
            num // i
        i += 2

    if num > 2:
        d += [num]
    return d

cnt = 0
for n in range(13_475_125, 10**30):
    F = fact(n)
    if len(F) == 5:
        cnt5 = 0
        for i in F:
            f = str(i)
            if f.count('5') >= 1:
                cnt5 += 1
        if cnt5 == 5:
            print(n,max(F))
            cnt += 1
            if cnt == 5:
                break