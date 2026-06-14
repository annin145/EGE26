ans = []
for N in range(1,100_000):
    R = oct(N)[2:]
    if R[0] == '5':
        R = R.replace('2', '*').replace('1','2').replace('*', '1')
        R = '11' + R
    else:
        R = '2' + R[1:] + '10'
    R = int(R,8)
    if R < 1354:
        ans.append([R,N])

print(max(ans))