ans = []
for N in range(1,100_000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[:3]
    else:
        r = (N % 3)*3
        r = bin(r)[2:]
        R = R + r
    R = int(R,2)

#     if R<140:
#         ans.append([N,R])
#
# print(ans)

# 31

    for h in range(120,140):
        if h == R:
            ans.append([N,R])
print(ans)
