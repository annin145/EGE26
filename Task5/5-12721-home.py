ans = []
for N in range(1,100_000):
    R = oct(N)[2:]
    if R.count('2') + R.count('4') + R.count('6') % 2 == 0:
        r = oct((N%8)*5)[2:]
        R = R + r
    else:
        R = R[-3:] + '46'
    R = int(R,8)
    if N >= 80:
        ans.append(R)
print(min(ans))