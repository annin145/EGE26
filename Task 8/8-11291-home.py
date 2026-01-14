from string import printable
from itertools import product

cnt = 0
for val in product(printable[:6], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('2') == 1:
            for i in val:
                if i in '2':
                    val = val.replace(i, '@')
                if i in '04':
                    val = val.replace(i,'!')
            if '!@' not in val and '@!' not in val:
                cnt += 1

print(cnt)
