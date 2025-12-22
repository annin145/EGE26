from itertools import product
from string import printable

cnt = 0
for val in product(printable[:8], repeat=10):
    val = ''.join(val)
    for i in printable[1:8:2]:
        val = val.replace(i, '*')
    if val[0] != '0' and val.count('7') == 5 and '*7' not in val and '7*' not in val and '77' not in val:
        cnt += 1
print(cnt)