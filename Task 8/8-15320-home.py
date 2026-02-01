from itertools import product

alph = sorted('парус')

for pos, val in enumerate(product(alph,repeat=5), start=1):
    val = ''.join(val)
    if val.count('у') <= 1 and 'аа' not in val:
            print(pos)

