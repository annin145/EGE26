from itertools import product
from string import printable
cnt = 0
for val in product(printable[:14],repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if val[-1] in '03':
            if len(set(val)) == 2:
                cnt +=1
print(cnt)