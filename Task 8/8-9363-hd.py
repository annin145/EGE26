from itertools import permutations

cnt = 0
for val in permutations('хочунабюджет'):
    val = ''.join(val)
    for i in 'оуаюе':
        val = val.replace(i,'#')
    if '#####' not in val:
        cnt += 1

print(cnt)