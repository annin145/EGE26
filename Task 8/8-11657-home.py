from string import printable
from itertools import *

cnt = 0
for val in product(printable[:8], repeat=6):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('3') == 0:
            if len(set(val)) == len(val):
                for i in val:
                    if i in '0246':
                        val = val.replace(i,'*')
                if '**' in val:
                    cnt += 1

print(cnt)