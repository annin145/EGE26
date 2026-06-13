from itertools import product
from string import printable

cnt = 0
for val in product(printable[:9], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('0') == 1:
        val = val.replace('3','*').replace('5','*').replace('7','*').replace('1', '*')
        if '*0' not in val and '0*' not in val:
            cnt += 1

print(cnt)