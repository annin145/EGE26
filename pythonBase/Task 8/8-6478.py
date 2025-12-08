from itertools import product

alph = 'моль'
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    val = val.replace('м', '*')
    val = val.replace('л','*')
    if val.count('ь') >= 1:
        if val[0] != 'ь' and '*ь' in val and 'ьь' not in val and 'оь' not in val :
            cnt += 1
    else:
        cnt += 1
print(cnt)