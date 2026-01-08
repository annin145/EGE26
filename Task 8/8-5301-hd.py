from itertools import product

cnt = 0
for val in product('леся ',repeat=5):
    val = ''.join(val)
    if val.count(' ') == 1:
        if val[-1] != ' ' and val[0] != ' ':
            for i in val:
                if i in 'ея':
                    val = val.replace(i, '*')
                if i in 'лс':
                    val = val.replace(i,'#')
            if '**' not in val and '##' not in val:
                cnt +=1

print(cnt)