from itertools import permutations

cnt = 0
for val in set(permutations('хочу сотку')):
    val = ''.join(val)
    if val[0] not in ' у' and ' у' not in val and val[-1] != ' ' :
        cnt += 1
print(cnt-1)