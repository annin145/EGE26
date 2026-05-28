from itertools import *

alph = sorted('строка')

for pos,val in enumerate(product(alph,repeat=5),start=1):
    val = ''.join(val)
    if val[0] not in 'ал' and val.count('с') == 1:
        if pos % 2 == 1:
            print(pos,val)
