from itertools import product

alph = sorted('гондубш')

for pos,val in enumerate(product(alph, repeat=7), start=1):
    val = ''.join(val)
    