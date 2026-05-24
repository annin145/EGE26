def dell(num):
    d = set()
    for i in range(1,int(num**.5)+1):
        if num % i == 0:
            d |= {i,num // i}
    if len(d) == 4:
        return d
    return 0

for n in range(178_965,178_982):
    F = dell(n)
    if F:
        print(sorted(F,reverse=True))


