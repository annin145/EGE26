from string import printable
def convert(num,sys):
    res = ''
    while num != 0:
        res += printable[num%sys]
        num //= sys
    return res [::-1]
ans = []
for N in range(1,10000):
    R = convert(N,8)
    if R[0] == '5':
        R = R.replace('2', '!')
        R = R.replace('1', '2')
        R = R.replace('!', '1')
        R = '11' + R
    else:
        R = '2' + R[1:] + '10'
    R = int(R,8)
    if R == 1352:
        ans.append(N)

print(max(ans))