from itertools import product

alph = 'алгоритм'

cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val.count('л') <= 1 and val[0] != 'р' and val[-1] != 'л' and val[-1] != 'г' and val[-1] != 'р' and val[-1] != 'т' and val[-1] != 'м':
        cnt += 1
print(cnt)

#75117