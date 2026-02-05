def is_prime(num):
    if num < 2: return False
    for i in range(2,int(num **.5)+1):
        if num % i == 0:
            return False
    return True

def fact(num):
    d = []
    i = 3

    while i*i < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d

cnt = 0
for n in range(5_000_001, 10**20, 2):
    M = fact(n)
    if len(M) == len(set(M)) == 2 and is_prime(M[1] - M[0]):
        print(n,max(M))
        cnt += 1
        if cnt == 5:
            break
