def f(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            d |= {i, num // i}
    if str(num) == str(num)[::-1]:
        if max(d) % 7 == 0:
            return max(d)
    return 0

cnt = 0
for n in range(10**9+1, 10**20):
    if F:= f(n):
        print(n, F)
        cnt += 1
        if cnt == 5:
            break