from itertools import product
from string import printable
cnt = 0
for val in product(printable[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if val[0] in '246' and val[-1] in '3456' and val.count('4') <= 1:
            cnt += 1

print(cnt)