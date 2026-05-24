from string import printable
from itertools import product

cnt = 0
for val in product(printable[:13], repeat=6):
    val = ''.join(val)
    if val[0] != '0':
        for i in 'abc':
            val = val.replace(i,'*')
        if val.count('0') >= 2 and val.count('*') == 2 and '**' in val:
            cnt += 1

print(cnt)