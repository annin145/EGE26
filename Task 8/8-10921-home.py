from itertools import permutations

cnt = 0
for val in set(permutations('ДЖаВАСКРИПТ')):
    val = ''.join(val)
    if (val.index('А') + val.index('а') + val.index('И') + 3)//2 == 11:
        cnt += 1

print(cnt)
############################################################
from itertools import permutations

cnt = 0
for val in set(permutations('ДЖАВАСКРИПТ')):
    val = ''.join(val)
    summ = 0
    for pos,b in enumerate(val,start=1):
        if b in 'AИ':
            summ += pos
    if summ == 11:
        cnt += 1

print(cnt)
#######################################################
from itertools import permutations

cnt = 0
for val in set(permutations('ДЖАВАСКРИПТ')):
    val = ''.join(val)
    if val.rfind('А') + val.rfind('А') + val.rfind('И') + 3 == 11:
        cnt += 1

print(cnt)