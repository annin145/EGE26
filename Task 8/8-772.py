from itertools import permutations

cnt = 0
for val in set(permutations('пробник')):
    val = ''.join(val)
    if val[0] in 'прбнк' and val[-1] in 'прбнк' and 'ои' not in val and 'ио' not in val:
        cnt += 1
print(cnt)