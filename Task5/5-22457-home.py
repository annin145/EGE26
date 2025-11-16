def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1,100_000):
    R = convert(N, 7)
    if sum(map(int,R)) % 2 == 0:
        R = R + '555'
    else:
        R = '33' + R + '6'
    R = int(R,7)
    if R < 12717:
        ans.append(N)
print(max(ans))