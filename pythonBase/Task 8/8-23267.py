from itertools import product

alph = sorted('строка')

for pos, val in enumerate(product(alph,repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in 'ал' and val.count('с') == 1 and pos % 2 == 1:
        print(pos)