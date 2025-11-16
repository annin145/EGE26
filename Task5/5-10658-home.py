def convert(num,sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res[::-1]

for N in range(1,100_000):
    R = convert(N,3)
    if  R.count('2') > R.count('1'):
        R = '22' + R
    else:
        R = '11' + R
    R = int(R,3)
    if R > 100:
        print(R)
        break

# 117