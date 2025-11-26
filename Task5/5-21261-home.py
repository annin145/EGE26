def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1,100_000):
    R = convert(N, 4)
    if sum(map(int, R)) % 3 == 0:
        R.replace('2', '*')
        R.replace('0', '2')
        R.replace('*', '0')
        R = R + '32'
    else:
        R = R + '33'
        r = R[2:3]
        r.replace(r , '1')
        n = R[3:4]
        n.replace(n, '0')
        #R = R[:1] + r + n + R[3:]
    R = int(R,4)
    if R == 335:
        print(N)

#20