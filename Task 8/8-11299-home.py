from itertools import product

for pos, val in enumerate(product('БМНРЮ', repeat = 6), start=1):
   val = ''.join(val)
   if pos % 2 != 0 and val[0] != 'М' and val.count('Р') >= 2 and 'Ю' not in val:
           print(pos)
#11719