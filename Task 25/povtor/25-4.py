def divs(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            d |= {i,num //i}

    for j in d:
        if j % 10 == 9 and j != 9 and j != num:
            return d
    return 0
cnt = 0
for N in range(800_001,10**10):
    if F := divs(N):
        cnt += 1
        print(N, min(i for i in F if i % 10 == 9 and i != 9 and i != N))
        if cnt == 5:
            break