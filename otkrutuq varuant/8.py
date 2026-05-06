from itertools import *

alph = sorted('апрель')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'л' and val[0] != 'а':
        if val.count('п') >= 2:
            if pos % 2 != 0:
                print(pos,val)
                break
