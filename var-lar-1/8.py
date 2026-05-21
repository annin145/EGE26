from itertools import product

alph = sorted('котена')
ans = []
for pos, val in enumerate(product(alph,repeat=7),start=1):
    val = ''.join(val)
    if val.count('к') == 2 and val.count('о') == 2 and val.count('т') == 1 and val.count('е') == 1 and val.count('н') == 1:
        if pos % 2 != 0:
            ans.append(pos)

print(max(ans))