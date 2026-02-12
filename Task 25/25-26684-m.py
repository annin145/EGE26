def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i *i < num + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 1:
        d += [num]
    return d

cnt = 0
for n in range(5_000_001, 10**30):
    if n % 100 == 12:
        d = fact(n)
        if len(d) - len(set(d)) == 5:
            print(n, min(d))
            cnt += 1
            if cnt == 5:
                break

            