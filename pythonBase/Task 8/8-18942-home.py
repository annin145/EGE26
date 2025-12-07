from itertools import product

alph = 'дионсй'

cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if 'д' in val and 'н' not in val or 'д' not in val and 'н' in val:
        if 'дд' not in val and 'ии' not in val and 'оо' not in val and 'нн' not in val and 'сс' not in val and  'йй' not in val:
            cnt += 1
            print(cnt)

# 8296