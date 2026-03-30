from string import printable
from itertools import product

cnt = 0
for val in product(printable[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        for i in val:
            if i in printable[:25:2]:
                val = val.replace(i,'@')
        for n in val:
            if n in printable[15:25]:
                val = val.replace(n,'!')
        if val.count('!') >= 2 and val.count('@') >= 1 :
            cnt += 1

print(cnt)