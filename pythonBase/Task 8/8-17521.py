from itertools import product
from string import printable

cnt = 0
for val in product(printable[:8], repeat=5):
    val = ''.join(val)
    if val[0] not in '01357' and val[-1] not in '26' and val.count('7') <= 2:
        cnt += 1
print(cnt)

#9135