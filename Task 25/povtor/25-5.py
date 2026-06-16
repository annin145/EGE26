def is_prime(num):
    if num < 2: return False
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            return False
    return True

def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num//=2

    i = 3
    while i*i <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    cnt = 0
    if len(d) == 2:
        for i in d:
            if str(i).count('5') == 1:
                cnt +=1
        if cnt == 2:
            return max(d)
    return 0

cnt = 0
for N in range(1_324_728, 10**10):
    if F := fact(N):
        cnt += 1
        print(N,F)
        if cnt == 5:
            break

