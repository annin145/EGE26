from string import printable
from itertools import permutations

cnt = 0
for val in permutations(printable[:10], r=4):
    val = ''.join(val)
    if val[0] != '0':
            for i in val:
                if i in '02468':
                    val = val.replace(i,'!')
                else:
                    val = val.replace(i,'#')
            if '!!' not in val and '@@' not in val:
                cnt += 1

print(cnt)
