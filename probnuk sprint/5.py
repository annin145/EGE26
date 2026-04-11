from string import printable

def convert(num,sys):
    res = ''
    while num:
        res += printable[num%sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1,100_000):
    R = convert(N,4)
    if N % 4 == 0:
        R = R[:2] + R
    else:
        r = (N % 4)*4
        r = convert(r,4)
        R = R + r
    R = int(R,4)
    if R > 291:
        ans.append(R)

print(min(ans))


