from itertools import product, repeat

alph = sorted('аожпюз')

ans = []

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'а' and val.count('з'):
        ans.append(pos)

print(len(ans))