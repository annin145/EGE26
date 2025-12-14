from itertools import permutations

cnt = 0
for val in set(permutations('запись')):
    val = ''.join(val)
    if val[0] not in 'ь' and 'аь' not in val and 'иь' not in val:
        cnt += 1
print(cnt)