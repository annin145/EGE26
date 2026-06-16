def divs(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            d |= {i,num // i}
    if len(d) >= 2:
        M = max(d) + min(d)
        if M % 10 == 4:
            return M
    return 0
cnt = 0
for n in range(800_001,10**10):
    if F := divs(n):
        cnt += 1
        print(n, F)
        if cnt == 5:
            break

