def divs(num):
    d = set()
    for i in range(2, int(num**.5)+1):
        if num % i == 0:
            d |= {i,num // i}
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 10 == 4:
            return M
    return 0
cnt = 0
for n in range(700_001, 10**10):
    if F := divs(n):
        print(n, F)
        cnt += 1
        if cnt == 5:
            break