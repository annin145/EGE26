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

    if (max(d) + min(d))%100 == 63 and (max(d) + min(d)) % len(d) == 0:
        return max(d)+ min(d)
    return 0

cnt = 0
for N in range(7_800_001,10**10):
    if M := fact(N):
        print(N,M)
        cnt += 1
        if cnt == 5:
            break
