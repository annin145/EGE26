def convert(num,sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res[::-1]

for N in range(1,100_000):
    R = convert(N,3)
    if N % 3 == 0:
        R =R + R[-2:]
    else:
        r = R.count('1') + R.count('2') + R.count('0')
        r = convert(r,3)
        R = R + r
    R = int(R,3)
    if R > 220:
        print(R)
        break

#222