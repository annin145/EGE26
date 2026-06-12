def DEL(num):
    for i in range(2, int(num**.5)+1):
        if num % i == 0:
            return i + num // i
    return 0


cnt = 0
for n in range(900_001,10**10):
    M = DEL(n)
    if M % 100 == 46:
        print(n, M)
        cnt += 1
        if cnt == 5:
            break