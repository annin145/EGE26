from itertools import *

alph = sorted('школа')

for pos,val in enumerate(product(alph,repeat=5),start=1):
    val = ''.join(val)
    if val in 'шалаш':
        print(pos,val)