from itertools import permutations

alph = 'парижанка'

cnt = 0
for val in set(permutations(alph, r=9)):
    val = ''.join(val)
    if val.count('аа') + val.count('иа') + val.count('аи') + val.count('ааа') == 1:
        cnt += 1
print(cnt)

#28800