from itertools import product

alph = sorted('теория')

for pos, val in enumerate(product(alph,repeat=6), start=1):
    val = ''.join(val)
    if val[0] not in 'ярт' and val.count('и') >= 2 and pos % 2 == 1:
        print(pos)