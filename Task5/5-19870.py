def convert(num,sys):
    if num == 0: return '0'
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res [::-1]

ans = []
for N in range(0,100_000):
    R = convert(N,4)
    if N % 2 == 0:
        r = int(R[-1])* 3
        r = convert(r, 4)
        R = '12' + R + r
    else:
        R = '13' + R + '21'
    R = int(R,4)

    if R > 50:
        ans.append(R)

print(min(ans))



