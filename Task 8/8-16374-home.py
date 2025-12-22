from itertools import product
from string import printable
cnt = 0
cnt1 = 0
for val in product(printable[:7], repeat=7):
    for i in val:
        if i in '0246':
            cnt1 +=1
    if cnt1 == 2:
        cnt += 1
    # if (val.count('0') + val.count('2') + val.count('4') + val.count('6')) ==2:


print(cnt)