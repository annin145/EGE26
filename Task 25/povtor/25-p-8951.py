def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i**2 <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    if len(d) == 3 and len(set(d)) == 3:
        cnt1 = 0
        for i in d:
            if (str(i). count('4') + str(i).count('7')) > 1:
                cnt1 += 1
        if cnt1 == 3:
            return max(d)
    return 0

cnt = 0
for n in range(2_400_001, 10**10):
    if F := fact(n):
        cnt += 1
        print(n, F)
        if cnt == 5:
            break
