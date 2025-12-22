from itertools import product

cnt = 0
alph = sorted('престол')
for pos,val in enumerate(product(alph, repeat=5), start =1):
    val = ''.join(val)
    if pos % 2 == 1 and val[-1] in 'ео' and (val.count('п') + val.count('р') + val.count('c') + val.count('т') + val.count('л')) <= 3:
            cnt +=1
print(cnt)