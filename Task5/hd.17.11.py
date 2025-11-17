def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = convert(N, 3)
    if N % 2 == 0:
        R = R + R[-2:]
    else:
        r = sum(map(int, R))
        r = convert(r, 3)
        R = R + r
    R = int(R, 3)
    if N > 9:
        ans.append((R, N))

print(min(ans))
