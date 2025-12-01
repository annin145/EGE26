ans = []
for N in range(151,100_000):
    R = hex(N)[2:]
    R = R.replace('a', '1')
    cnt = 0
    for i in R:
        if int(i,16) % 2 == 0:
            cnt += 1
    if cnt > 2:
        R = R + 'b'
    else:
        R = 'f' + R
    R = int(R, 16)
    if R == 3856:
        ans.append(N)
print(min(ans))



