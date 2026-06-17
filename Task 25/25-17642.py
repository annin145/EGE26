def divs(num):
    d = set()
    for i in range(2, int(num**.5)+1):
        if num % i == 0:
            d |= {i,num // i}
    cnt1 = 0
    for i in d:
        if i % 10 == 9 and i != 9 and i != num:
            cnt1 += 1
        if cnt1 == 1:
            return min(i for i in d if i % 10 == 9 and i != 9 and i != num)
    return 0
cnt = 0
for n in range(800_001, 10**10):
    if F := divs(n):
        cnt += 1
        print(n, F)
        if cnt == 5:
            break