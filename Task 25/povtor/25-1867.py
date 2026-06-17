def divs(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            d |= {i,num // i}
    cnt = 0
    for i in d:
        if i % 10 == 8 and i != 8 and i != num:
            cnt += 1
        if cnt == 1:
            return d
    return 0
cnt5 = 0
for n in range(500_001, 10**10):
    if F := divs(n):
        print(n, min(i for i in F if i % 10 == 8 and i != 8 and i != n) )
        cnt5  += 1
        if cnt5 == 5:
            break