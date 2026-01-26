from fnmatch import fnmatch

for N in range(12347 - 12347 % 141,10**8,141):
    if fnmatch(str(N), '1234*7'):
        print(N,N//141)

####################################
from itertools import product
from string import printable

for l in range(0,4):
    for val in product(printable[:10], repeat=l):
        val = int('1234' + ''.join(val) + '7')
        if val % 141 == 0:
            print(val,val//141)
