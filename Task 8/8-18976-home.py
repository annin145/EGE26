from itertools import  product
cnt = 0
for i in product([i for i in range(20)],repeat = 5):
    if i[0] != 0:
        if all(i[p] % 2 != i[p+1] % 2 for p in range(4)) and (i[0]+i[-1]) == 26:
            cnt += 1
print(cnt)

#13000