for N in range(1,100_000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + '00'
    else:
        R = R + '11'
    R = int(R, 2)
    if R < 94:
        print(N)
#22