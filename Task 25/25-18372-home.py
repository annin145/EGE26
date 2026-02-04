
def f(num):
    d = set()
    for i in range(2,int(num ** .5)+1):
        if num % i == 0:
            d |= {i,}
            if num // i != num:
                d |= {num // i}
    return sum(d) // len(d)

cnt = 0
for n in range(1,770_000)[::-1]:
    A = f(n)
    if A % 100 == 12:
        print(n, A)
        cnt += 1
        if cnt == 5:
            break

