from itertools import *

alph = 'полина'
cnt = 0
for val in product(alph, repeat=8):
    val = ''.join(val)
    soglas = val.count('п')+val.count('л')+val.count('н')
    glas = val.count('о')+val.count('и')+val.count('а')
    if soglas > glas:
        cnt += 1

print(cnt)

#610173