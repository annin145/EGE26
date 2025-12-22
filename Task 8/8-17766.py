from itertools import product

alph = sorted('сентябрь')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'р' and val.count('ь') == 0:
        print(pos)