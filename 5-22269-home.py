def convert (num, sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 5)
    if R[-1:] == '0':
        R = R.replace('4', '*')
        R = R.replace('1', '4')
        R = R.replace('*','1')
        R = '33' + R
    else:
        R = '3' + R[1:] + '42'
    R = int(R,5)
    if R < 1922:
        ans.append([R,N])

max = max(ans)[0]
for i in ans:
    if i[0] == max:
        print(i[1])

#9