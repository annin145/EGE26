def DEL(num):
    d = set()
    for i in range(1, int(num**.5)+1):
        if num % i == 0:
            d |= {i,num//i}
    return d
cnt = 0
for N in range(700_001,10**10):
    F = DEL(N)
    for i in F:
        if i % 10 == 7 and i != 7 and i != N:
            cnt += 1
            print(N, min(i for i in F if i % 10 == '7' and i != 7 and i != N))
            if cnt == 5:
                break

