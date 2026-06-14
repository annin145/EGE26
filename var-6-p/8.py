from string import printable
from itertools import product

cnt = 0
for val in product('0123456', repeat=7):
    val = ''.join(val)
    if val[0] !='0' and sum(val.count(c) for c in '0246') == 2:
            cnt += 1

print(cnt)