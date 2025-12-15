def convert (num,sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res [::-1]

ans = []
for N in range(1,100_000):
    R = convert(N,3)
    if N % 3 == 0:
        r = R[-2:]
        R = R + r
    else:
        r3 = (R.count('1') + R.count('2')*2)*3
        r3 = convert(r3,3)
        R = R + r3
    R = int(R,3)
    if R > 208 and R % 2 == 1:
        ans.append(R)
print(min(ans))
