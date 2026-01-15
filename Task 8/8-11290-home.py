from itertools import product
from string import printable

cnt = 0
for val in product(printable[:16], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('9') == 1:
            for i in val:
                if i in '02468ace':
                    val = val.replace(i, '#')
                else:
                    val = val.replace(i,'*')
            if '##' not in val and '**' not in val:
                cnt +=1
print(cnt)