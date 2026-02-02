ans = []
for N in range(1,1000):
    R = bin(N+2)[2:]
    r = R.count('1') % 2
    R = R + str(r)
    rn = R.count('1') % 2
    R = R+str(rn)
    R = int(R,2)

    if R < 61:
        ans.append(N)

print(max(ans))