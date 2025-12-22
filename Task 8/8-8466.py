from itertools import product
from string import printable

cnt = 0
for val in product(printable[:7], repeat=6):
    val = ''.join(val)
    ch = 0
    nch = 0
    if val[0] != '0':
        if val[-1] not in '0123':
            for i in val:
                if i in '0246':
                    ch +=1
                else:
                    nch += 1
            if ch == nch:
                cnt +=1
print(cnt)