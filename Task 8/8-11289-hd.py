from itertools import *
from string import printable

cnt = 0
for val in product(printable[:9], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('2') == 0:
            if len(set(val)) == len(val):
                for i in val:
                    if i in '02468':
                        val = val.replace(i,'@')
                    else:
                        val = val.replace(i,'!')
                if '!!' not in val and '@@' not in val:
                    cnt += 1
print(cnt)