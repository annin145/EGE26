from itertools import product, repeat

alph = 'кайф'

cnt = 0
for val in product(alph,repeat=4):
    val = ''.join(val)
    if val.count('к') == 1 and val.count('а') == 1 and val.count('й') == 1 or val.count('ф') == 1:
        if val[-1] not in 'й':
            if val[0] not in 'к' and val[1] not in 'ф' or val[1] not in 'к' and val[2] not in 'ф' or val[2] not in 'к' and val[3] not in 'ф':
                cnt +=1

print(cnt)