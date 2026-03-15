from itertools import *

alph = sorted('цитрус')

ans = []
for pos, val in enumerate(product(alph, repeat=5),start=1):
    val = ''. join(val)
    if val.count('и') == 2:
        for i in val:
            if 'ц' in val:
                val = val.replace(i,'!')
        if '!!' not in val:
            ans.append(pos)

print(max(ans))