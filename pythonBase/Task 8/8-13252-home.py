from itertools import permutations

alph = 'кидала'

cnt = 0
for val in set(permutations(alph, r=5)):
    val = ''.join(val)
    if 'аа' not in val and 'кк' not in val and 'ии' not in val and 'дд' not in val and 'лл' not in val:
        cnt += 1
print(cnt)

#264