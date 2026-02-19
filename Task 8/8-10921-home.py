from itertools import permutations

cnt = 0
for val in set(permutations('ДЖаВАСКРИПТ')):
    val = ''.join(val)
    if val.index('А') + val.index('а') + val.index('И') + 3 == 11:
        cnt += 1

print(cnt)