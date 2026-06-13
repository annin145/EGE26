def fast(num):
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

for n in range(3_700_001,10**10):
    M = fast(n)
    if len(M) == len(set(M)) == 2 and M[1] - M[0] == 2 or sum(M) == 5:
        print(n,sum(M))
        cnt += 1
        if cnt == 5:
            break