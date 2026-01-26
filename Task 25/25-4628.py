from fnmatch import fnmatch

for n in range(124065 - 124065 % 161, 10**8,161):
    if fnmatch(str(n), '12*4?65'):
        print(n,n//161)

######################################
from string import printable
from itertools import product
# 100000000
# 12*4?65

# 12z4v65
ans = []
for v in printable[:9]:
    for l in range(0,3):
        for z in product(printable[:10], repeat=l):
            num = int('12'+ ''.join(z) + '4' + v + '65')
            num = int(f'12{''.join(z)}4{v}65')
            if num % 161 == 0:
                ans.append([num,num//161])

for i in sorted(ans):
    print(*i)