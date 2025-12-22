from string import printable
from itertools import product

cnt = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in '0369':
            val = val.replace(i, '*')
        for i in '124578ab':
            val = val.replace(i,'#')
        # i = -1
        # r = int(val[i], 12)
        # if r % 3 == 0 or r == 0:
        #     val3 = val.replace('r', '*')
        #     i -= 1
        # else:
        #     val3 = val.replace('r', '#')
        #     i -= 1
        if '**' not in val and '##' not in val:
            cnt += 1
print(cnt)