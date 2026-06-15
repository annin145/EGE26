from itertools import product

alph = sorted('аргумент')
cnt = 0
for pos,val in enumerate(product(alph,repeat=4), start=1):
    val = ''.join(val)
    if len(val) == len(set(val)) and val in 'нрту':
        cnt += 1
        print(pos, val)
print(alph)
print()
