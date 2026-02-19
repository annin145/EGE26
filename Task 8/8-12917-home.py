from itertools import permutations

alph = 'просто'

cnt = 0
for val in set(permutations(alph, r=5)):
    val = ''.join(val)
    if 'ОО' not in val:
        cnt += 1

print(cnt)