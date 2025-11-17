ans = []
for N in range(1,100_000):
    R = bin(N)[2:]
    if N % 8 == 0:
        R = R + R[-2:]
    else:
        n = (N % 8)*2
        n = bin(n)[2:]
        R = R + n
    R = int(R,2)
    if R > 3000:
        ans.append(N)
print(min(ans))