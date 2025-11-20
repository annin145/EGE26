def convert(num,sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1,100_000):
    R = convert(N,3)
    r = R.count('1') + R.count('2')*2
    if r % 3 == 0:
        R = R +'212'
    else:
        r = r*2
        r = convert(r,3)
        R = R + r
    R = int(R,3)
    if R > 490:
        ans.append(R)
print(min(ans))