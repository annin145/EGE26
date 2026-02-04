def is_prime(num):
    if num < 2: return False
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num//i):
                d |= {num % i}


    s = 0
    for i in d:
        s += i
    if s % 145 == 0:
        return s
    return 0

cnt = 0
for n in range(32_500_001, 10**30):
    if F := f(n):
        cnt += 1
        print(n, F)
        if cnt == 7:
            break