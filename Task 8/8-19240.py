from itertools import product

alph = sorted('январь')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    val = val.replace('я', '*')
    if val[0] != '*' and val.count('ь') <= 1 and '**' not in val:
        print(pos)