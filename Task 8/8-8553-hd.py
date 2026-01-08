from itertools import product

alph = sorted('нормалье')

cnt = 0
norm = 0
nenorm = 0
for pos,val in enumerate(product(alph, repeat=6),start=1):
    val = ''.join(val)
    if val[:6] == 'ненорм':
        nenorm = pos
    if val[:4] == 'норм':
        norm = pos
        break

print(norm - nenorm)