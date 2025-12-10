from itertools import product

alph = sorted('сублимаця')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    glas = val.count('у') + val.count('и') + val.count('а') + val.count('я')
    if val[-1] != 'я' and glas == 2 and pos % 2 == 1:
        print(pos)

#58955