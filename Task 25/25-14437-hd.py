def f(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            d |= {i,num//i}
    if d:
        M = sum(d) // len(d)
        if M % 1000 == 313:
            return M
    return 0

cnt = 0
for n in range(1,700_000)[::-1]:
    if M := f(n):
        print(n,M)
        cnt += 1
        if cnt == 7:
            break

