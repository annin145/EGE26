for N in range(1,100_000):
    R = bin(N)[2:]
    if N % 2 == 0:
        r = R.count('1')
        r = bin(r)[2:]
        R = R + r
    else:
        R = '1' + R + '101'
    R = int(R, 2)
    if R > 350:
       print(N)
       break

# 17