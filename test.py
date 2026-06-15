# L = 25
# N = 26
# i = 5
# n = 35
# I = 25*5/8
# print(I)
# print(16*35)
from math import *
#########################################
for L in range(1,10**10):
    N = 27
    i = ceil(log(N,2))
    I = ceil(L * i/8)
    if I * 7_564_230 > 31*2**20:
        print(L)
        break

for L in range(1,10**10):
    N = 37
    i = ceil(log(N,2))
    I = ceil(L*i/8)
    if I * 3548 > 12*1024:
        print(L)
        break

######################################
for N in range(1,10**10):
    L = 172
    i = ceil(log(N,2))
    I = ceil(L*i/8)
    if I * 356_984 <= 54*1024*1024:
        print(N)
        break

