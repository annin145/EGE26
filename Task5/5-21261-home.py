def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res[::-1]

for N in range(1,100_000):
    R = convert(N, 4)
    if sum(map(int, R)) % 3 == 0:
        R = R.replace('2', '*')
        R = R.replace('0', '2')
        R = R.replace('*', '0')
        R ='32' + R
    else:
        R = R + '33'
        R = R[0] + '10' + R[3:]
    R = int(R, 4)
    if R == 335:
        print(N)

