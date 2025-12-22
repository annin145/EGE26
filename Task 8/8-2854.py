from itertools import permutations

cnt = 0
for val in set(permutations('росомаха', r=8)):
    val = ''.join(val)
    if 'оо' not in val and 'аа' not in val and 'оа' not in val and 'ао' not in val:
        for i in 'рсмх':
            val = val.replace(i, '*')
        if '**' not in val:
            cnt += 1
print(cnt)