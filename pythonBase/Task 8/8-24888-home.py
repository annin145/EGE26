from itertools import product
from string import printable

cnt = 0
for val in product(printable[:16], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 1 and '00' not in val and '00' not in val and '11' not in val and '22' not in val and '33' not in val and '44' not in val and '55' not in val and '66' not in val and '77' not in val and '88' not in val and '99' not in val and 'aa' not in val and 'bb' not in val and 'cc' not in val and 'dd' not in val and 'ee' not in val and 'ff' not in val:
        cnt += 1
print(cnt)

#11564