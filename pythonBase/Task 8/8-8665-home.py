from string import printable
from itertools import product

chit = '02468ac'
cnt = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('b') == 2:
            for i in val:
                if i in chit:
                    val = val.replace(i, '*')
                else:
                    val = val.replace(i, '#')
            if '*#*#*#*' in val or '#*#*#*#' in val:
                cnt += 1
print(cnt)

#48600