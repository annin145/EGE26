def is_prime(num):
    if num < 2: return False
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            return False
    return True

def prime_divs(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num//i):
                d |= {num //i}
    if len(d) >= 2:
        M = min(d) + max(d)
        if M > 60_000 and str(M) == str(M)[::-1]:
            return M
    return 0
cnt = 0
for N in range(5_400_001,10**10):
    if F := prime_divs(N):
        cnt += 1
        print(N,F)
        if cnt == 5:
            break





