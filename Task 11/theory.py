from math import log2, ceil
# 1855
N = 5_000
L = 101
i = ceil(log2(N)) # bit
I = ceil((L * i)/8) # byte
print(I*2048 / 1024)

# 23270
for L in range(1,100_000):
    N = 37
    i = ceil(log2(N)) # bit
    I = ceil((L * i)/8) # byte
    if 3548 * I > 12 * 1024:
        print(L)
        break

#23195
for N in range(1,100_000):
    L = 172
    i = ceil(log2(N)) # bit
    I = ceil((L * i)/8) # byte
    if 356_984 * I >= 54*1024*1024:
        print(N)
        break