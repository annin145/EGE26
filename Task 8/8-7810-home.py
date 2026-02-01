from itertools import product

alph = 'масло'

cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val.count('а') + val.count('о') == 1:
        cnt += 1

print(cnt)