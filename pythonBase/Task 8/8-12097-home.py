from itertools import product

alph = sorted('гирлянда')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val.count('д') == 3 and val[0] != 'я':
        print(pos)
