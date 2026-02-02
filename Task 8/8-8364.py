from itertools import *

alph = sorted('крате')

for pos,val in enumerate(product(alph, repeat=6),start=1):
    val = ''.join(val)
    if val in 'карета':
        print(val,pos)
    if val  in 'ракета':
        print(val,pos)

print(9670-6670-1)