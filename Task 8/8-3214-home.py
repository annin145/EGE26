from itertools import product

alph = sorted('парус')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    #val = val.replace('а', '*')
    if val[0] == 'у' and 'аа' not in val:
        print(pos)

#2527