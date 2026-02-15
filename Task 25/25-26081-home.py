def ssum(num):
    for i in range(113,999_999+1):
        if i % 113 == 0:
            for x in range(1,13):
                if i + 3**x == num:
                    return x
    return 0

cnt = 0
for n in range(100_001, 1_000_000):
    F = ssum(n)
    if str(n).count('0') == 0:
        print(n,F)
        cnt += 1
        if cnt == 5:
            break