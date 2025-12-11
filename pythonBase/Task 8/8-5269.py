from itertools import permutations

cnt = 0
for val in set(permutations('амфибрахий')):
    val = ''.join(val)
    if val[len(val) // 2] in 'б' and val[len(val) // 2 + 1] in 'р':
        cnt += 1
print(cnt)