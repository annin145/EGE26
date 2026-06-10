from itertools import product
from string import printable
cnt = 0
for val in product(printable[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('6') == 1:
            if val[0] != val[1] and val[1] != val[2] and val[2] != val[3] and val[3] != val[4]:
                    cnt +=1

print(cnt)

print(printable[:7])
