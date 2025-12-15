from itertools import product

alph = sorted('гранит')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 1 and val[0] not in 'аги' and val.count('а') == 1:
        print(pos)