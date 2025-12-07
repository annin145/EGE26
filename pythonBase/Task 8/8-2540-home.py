from itertools import product

alph = sorted('автор')

for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if val == 'вата':
        print(pos)

# 146