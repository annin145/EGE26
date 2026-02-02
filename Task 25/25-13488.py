def f(num):
    d = set()
    for i in range(2,int(num ** .5) + 1):
        if num % i == 0:
            if i % 2 == 1:
                d |= {i}
            if num // i % 2 == 1:
                d |= {num//i}

    if len(d) == 3:
        return d
    return set()

for n in range(18_782, 18_823):
    if M := f(n):
        print(*sorted(M))
