for N in range(1,100_000):
    R = bin(N)[2:]
    if N % 5 == 0:
        R = R + R[3::-1]
    else:
        r = (N % 5)*5
        r = bin(r)[2:]
        R = R + r
    R = int(R,2)
    if R > 256:
        print(N)
        break