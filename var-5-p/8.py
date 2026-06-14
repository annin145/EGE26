from itertools import product

alph = sorted('аргумент')

for pos,val in enumerate(product(alph,repeat=4), start=1):
    val = ''.join(val)

