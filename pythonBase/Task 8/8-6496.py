from itertools import product

alph = 'берск'

for pos, val in enumerate(product(alph, repeat=7)):
    val = ''.join(val)
    print(pos)
