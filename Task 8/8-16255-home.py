from itertools import product
from string import printable

cnt = 0
for val in product(printable[:9], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val[0] not in '1357' and val[-1] not in '036' and val.count('6') >= 1:
            cnt +=1

print(cnt)

#827352