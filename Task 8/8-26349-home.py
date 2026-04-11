from itertools import product
for n in range(1, 20):
    a = [''.join(x) for x in product('сулак', repeat=n)]
    a.sort()
    i = 0
    for x in a:
        i += 1
        x = x.replace('у', '*').replace('а', '*')
        if i % 2 == 0 and x[0] in 'лс' and x.count('*') <= 2 and '**' not in x:
            m = i
    if  m == 12368:
        print(n)
        break
