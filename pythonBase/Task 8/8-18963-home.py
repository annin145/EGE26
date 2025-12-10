from itertools import product

alph = 'котбус'

cnt = 0
for val in product(alph, repeat=8):
    val = ''.join(val)
    if 'кот' in val and val[0] != 'у' and  val[0] != 'о':
        cnt += 1
print(cnt)

#33516