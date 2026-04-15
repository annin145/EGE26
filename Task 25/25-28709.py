def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i =3
    while i < int(num ** .5)+1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]
    return d

cnt = 0
for n in range(6_300_001, 10**20):
    f = fact(n)
    if len(f) == 3:
        u = [1 for i in f if '3' in str(i) or '4' in str(i)]
        if sum(u) == 3:
            cnt += 1
            print(n,max(f))
            if cnt == 5:
                break
