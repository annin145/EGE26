for N in range(1, 100_000):
    R = hex(N)[2:]
    cnt = 0
    for i in R:
        if i == 'b':
            cnt += 1
        if cnt % 2 == 0:
            R = '1' + R
        else:
            R = R + '1'
    R = int(R,16)
    cnt = 0
    if len(str(R)) == 2:
        cnt += 1

print(cnt)