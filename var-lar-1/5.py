from string import printable
def convert(num,sys):
    res = ''
    while num != 0:
        res += printable[num%sys]
        num //=sys
    return res[::-1]
ans = []
for N in range(1, 100_000):
    R = convert(N,3)
    if N % 5 == 0:
        R = R + R[-2:]
    else:
        r = (N % 5)*7
        r = convert(r,3)
        R = R + r
    R = int(R,3)
    if R < 200:
        ans.append(N)

print(sum(ans)/len(ans))
