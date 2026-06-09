def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i < int(num**.5)+1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    return d

cnt = 0
for n in range(6_651_221,10**10):
    d = fact(n)
    if len(d) == 2:
        if str(d[0]).count('2') == 1 and str(d[1]).count('2') == 1:
            print(*sorted([n,max(d)]))
            cnt += 1
            if cnt == 5:
                break



