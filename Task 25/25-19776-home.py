def f(num):
    d = set()
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            d |= {i,num//i}
    return sorted(d)

cnt = 0
for x in range(23_600_001,23_601_000):
    d = [i for i in f(x) if len(f(i))==0]
    M = d[0]+d[-1] if len(d)>0 else 0
    if M % 213 == 171:
        print(x,M)
        cnt += 1
        if cnt ==6:
            break

